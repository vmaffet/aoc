rucksacks = string(importdata('input.txt'));

sizes = strlength(rucksacks);

compartment1 = extractBefore(rucksacks, sizes/2+1);
compartment2 = extractAfter(rucksacks, sizes/2);

items = cellfun(@intersect, cellstr(compartment1), cellstr(compartment2));

part1 = sum(priority(items))

elfs1 = rucksacks(1:3:length(rucksacks));
elfs2 = rucksacks(2:3:length(rucksacks));
elfs3 = rucksacks(3:3:length(rucksacks));

badges = cellfun(@intersect,...
                 cellfun(@intersect,...
                         cellstr(elfs1),...
                         cellstr(elfs2),...
                         'UniformOutput',false),...
                 cellstr(elfs3));

part2 = sum(priority(badges))

function p = priority(item)
    p = item - 'a' + 1 + ('a' - 'A' + 26)*isstrprop(item, 'upper');
end
