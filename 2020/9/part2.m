numbers = readmatrix('input.txt', 'OutputType','uint64');

objective = uint64(3199139634);

pre_sum = [0; cumsum(numbers)];
seq_sum = pre_sum - pre_sum' - diag(numbers, -1);

[stop,start] = find(seq_sum == objective);
seq = numbers(start:stop-1);

R = min(seq) + max(seq)