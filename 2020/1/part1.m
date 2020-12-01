load input.txt

S = input + input';
M = S == 2020;
[idx_A, idx_B] = find(M, 1);

A = input(idx_A);
B = input(idx_B);

R = A*B
