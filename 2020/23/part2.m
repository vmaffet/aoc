cups = int32(num2str(readmatrix('input.txt')) - '0');

n_cups = int32(1000000);
cups = [cups max(cups)+1:n_cups];

[~, order, ~] = unique(cups);
next = cups(mod(order, numel(cups)) + 1);

current = cups(1);

n_moves = 10000000;

for i = 1:n_moves
    
    pick_1 = next(current);
    pick_2 = next(pick_1);
    pick_3 = next(pick_2);
    
    next(current) = next(pick_3);
    
    dest = mod(current - 2, n_cups) + 1;
    while dest == pick_1 || dest == pick_2 || dest == pick_3 || dest < 1
        dest = mod(dest - 2, n_cups) + 1;
    end
    
    tmp = next(dest);
    next(dest) = pick_1;
    next(pick_3) = tmp;

    current = next(current);
    
end

R = uint64(next(1)) * uint64(next(next(1)))