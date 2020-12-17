pocket = cell2mat(importdata('input.txt')) == '#';

kernel = ones(3, 3, 3, 3);
kernel(2, 2, 2, 2) = 0;

cycles = 6;

for k = 1:cycles

    pocket = padarray(pocket, [1,1,1,1], 0);
    neighbors = convn(pocket, kernel, 'same');

    three = neighbors == 3;
    two = neighbors == 2;

    pocket = three | (two & pocket);

end

R = sum(pocket, 'all')