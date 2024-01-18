#!/usr/bin/python3

import z3

positions, velocities = [], []
with open('input.txt', 'r') as f:
    for line in f:
        p, v = line.split('@')
        positions.append(tuple(map(int, p.split(','))))
        velocities.append(tuple(map(int, v.split(','))))

# y = a*x + b
def ab(x, y, dx, dy):
    a = dy / dx
    b = y - a * x
    return (a, b)

# ==== Part 1 ==== #
cnt = 0
N = len(positions)
for i, ((xi, yi, _), (dxi, dyi, _)) in enumerate(zip(positions, velocities)):
    (ai,bi) = ab(xi, yi, dxi, dyi)
    for (xj, yj, _), (dxj, dyj, _) in zip(positions[i+1:], velocities[i+1:]):
        (aj,bj) = ab(xj, yj, dxj, dyj)
        if ai != aj:
            x = (bj - bi) / (ai - aj)
            y = ai * x + bi
            if (x - xi)/dxi > 0 \
                    and (x - xj)/dxj > 0 \
                    and 200000000000000 <= x <= 400000000000000 \
                    and 200000000000000 <= y <= 400000000000000:
                cnt += 1

print(cnt)

# ==== Part 2 ==== #
x, y, z = z3.Real('x'), z3.Real('y'), z3.Real('z')
dx, dy, dz = z3.Real('dx'), z3.Real('dy'), z3.Real('dz')
time = z3.RealVector('t', 3)

s = z3.Solver()
for t, (xi, yi, zi), (dxi, dyi, dzi) in zip(time, positions, velocities):
    s.add(*[
        x + dx * t == xi + dxi * t,
        y + dy * t == yi + dyi * t,
        z + dz * t == zi + dzi * t
    ])
s.check()

print(s.model().eval(x + y + z))
