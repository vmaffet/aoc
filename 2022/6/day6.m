input = fileread('input.txt');

n = length(input);

nodup = @(s) isequal(s, unique(s,'stable'));

idx4 = (1:n-3)' + (0:3);
part1 = 3 + find(cellfun(nodup, cellstr(input(idx4))), 1)

idx14 = (1:n-13)' + (0:13);
part2 = 13 + find(cellfun(nodup, cellstr(input(idx14))), 1)
