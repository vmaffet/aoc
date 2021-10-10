#!/usr/bin/python3
import argparse
import re
from dataclasses import dataclass
from typing import Type
import copy

parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of your input file")
parser.add_argument("-p", "--part", help="part number", type=int, default=1)
args = parser.parse_args()

p = re.compile(r"(\d+) units each with (\d+) hit points (?:\((\w+ to [\w, ]+)?(?:; )?(\w+ to [\w, ]+)?\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)")

@dataclass
class Group:
    units: int
    hit_points: int
    weaknesses: set[str]
    immunities: set[str]
    attack_damage: int
    attack_type: str
    initiative: int
    id: int
    team: str
    target: Type['Group'] = None
    attacker: Type['Group'] = None

    def reset(self):
        self.target = None
        self.attacker = None

    def is_alive(self) -> bool:
        return self.units > 0

    def is_weak_to(self, source) -> bool:
        return source.attack_type in self.weaknesses

    def is_immune_to(self, source) -> bool:
        return source.attack_type in self.immunities

    def is_enemy(self, other) -> bool:
        return self.team != other.team

    def effective_power(self) -> int:
        return self.units * self.attack_damage

    def damage_to(self, target) -> int:
        mul = 1
        if target.is_immune_to(self): mul = 0
        elif target.is_weak_to(self): mul = 2
        return self.effective_power() * mul

    def selection_order(self) -> tuple[int, int]:
        return (self.effective_power(), self.initiative)

    def attack_order(self) -> int:
        return self.initiative

    def target_order(self, target) -> tuple[int, int, int]:
        return (self.damage_to(target), target.effective_power(), target.initiative)

    def select_target(self, enemies):
        is_targetable = lambda g: g.is_alive() and g.is_enemy(self) and not g.attacker and self.damage_to(g) > 0
        targetable = filter(is_targetable, enemies)
        try:
            self.target = max(targetable, key=self.target_order)
            self.target.attacker = self
        except ValueError:
            pass # There was no possible groups

    def attack_target(self):
        if self.target:
            dmg = self.damage_to(self.target)
            units_killed = min(self.target.units, dmg // self.target.hit_points)
            self.target.units -= units_killed

    def __repr__(self):
        return f"{self.team} Group {self.id} contains {self.units} units"


groups = []
with open(args.file, 'r') as f:
    for line in f:
        if ":" in line:
            next_id = 1
            next_team, *_ = line.partition(":")
        elif not line.isspace():
            m = p.match(line)
            (n, hp, wr, rw, ad, ap, i) = m.groups()
            w = set()
            r = set()
            if wr:
                if wr.startswith('weak to'):
                    w |= set(wr[8:].split(', '))
                else:
                    r |= set(wr[10:].split(', '))
            if rw:
                if rw.startswith('weak to'):
                    w |= set(rw[8:].split(', '))
                else:
                    r |= set(rw[10:].split(', '))

            group = Group(int(n), int(hp), w, r, int(ad), ap, int(i), next_id, next_team)
            groups.append(group)
            next_id += 1


def fight(army, boost=0):

    # Applying boost
    for g in army:
        if g.team == "Immune System":
            g.attack_damage += boost

    state = -1
    while True:
        # Target Selection
        [g.select_target(army) for g in sorted(army, key=Group.selection_order, reverse=True)]

        # Attack
        [g.attack_target() for g in sorted(army, key=Group.attack_order, reverse=True)]

        # Clean up for next fight
        [g.reset() for g in army]

        infection_units = sum(g.units for g in army if g.team == "Infection")
        immune_system_units = sum(g.units for g in army if g.team == "Immune System")
        if infection_units == 0 or immune_system_units == 0 or immune_system_units + infection_units == state:
            break

        state = immune_system_units + infection_units

    return (immune_system_units, infection_units)


if args.part == 1:
    print(max(fight(groups)))

elif args.part == 2:
    low, high = 0, float('inf')
    boost = 1
    units_left = 0
    while high - low > 1:
        new_groups = copy.deepcopy(groups)
        (immune_system_units, infection_units) = fight(new_groups, boost)

        if infection_units == 0:
            high = boost
            units_left = immune_system_units
        else:
            low = boost
            if high == float('inf'):
                boost *= 2
                continue
        
        boost = (high + low) // 2
    
    print(units_left)
