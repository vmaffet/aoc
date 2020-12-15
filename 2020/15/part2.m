starting = readmatrix('input.txt');

target = 30000000;
seen = zeros(target+1,1);
seen(starting+1) = 1:length(starting);

next = 0;
for i = length(starting)+1:target-1
    
    tmp = seen(next+1);
    seen(next+1) = i;
    if tmp == 0
        next = 0;
    else
        next = i - tmp;
    end
    
end

R = next