load input.txt

[ONE, TWO, THREE] = meshgrid(input);
S = ONE + TWO + THREE;
M = S == 2020;
idx = find(M, 1);

[idx_A, idx_B, idx_C] = ind2sub(size(M), idx);

A = input(idx_A);
B = input(idx_B);
C = input(idx_C);

R = A*B*C