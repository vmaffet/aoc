numbers = readmatrix('input.txt', 'OutputType','uint64');

preamble = 25;

sums = numbers(1:preamble) + numbers(1:preamble)';
sums(eye(preamble, 'logical')) = 0;

for k = preamble+2:length(numbers)

    previous = numbers(k-preamble:k-1);
    new_sum = previous(1:end-1) + previous(end);
    
    sums = [sums(2:end, 2:end) new_sum
            new_sum'           0      ];
    
    if all(sums ~= numbers(k), 'all')
        break
    end
end

R = numbers(k)