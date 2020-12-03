M = cell2mat(importdata('input.txt'));

r = 3;
d = 1;

[height, width] = size(M);

down = 1:d:height;
N = length(down);
right = linspace(1, 1+r*(N-1), N);

ind = sub2ind(size(M), down, mod(right-1, width) + 1);

locations = M(ind);

R = count(locations, '#')