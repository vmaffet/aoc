starting = readmatrix('input.txt');

target = 2020;
seen = zeros(target+1,1);
seen(starting+1) = 1:length(starting);

next = 0;
for i = length(starting)+1:target-1
    
    tmp = seen(next+1);
    seen(next+1) = i;
    
    next = (tmp ~= 0) * (i - tmp);
    
end

R = next