input = fileread('input.txt');

elfs = split(input, whitespacePattern(4));
elfs = cellfun(@str2num, elfs, 'UniformOutput',false);

calories = cellfun(@sum, elfs);

part1 = max(calories)
part2 = sum(maxk(calories, 3))
