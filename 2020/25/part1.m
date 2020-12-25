public_keys = readmatrix('input.txt');

loop_sizes = [0;0];

n = 20201227;

i = 1;
p = 1;
while all(loop_sizes == 0)
    p = mod(p * 7, n);
    loop_sizes(public_keys == p) = i;
    i = i + 1;
end

sel = loop_sizes ~= 0;

R = powermod(public_keys(~sel), loop_sizes(sel), n)