adapters = readmatrix('input.txt');
adapters = [0; sort(adapters)];

gaps = [diff(adapters); 3];

R = sum(gaps == 1) * sum(gaps == 3)