cups = num2str(readmatrix('input.txt')) - '0';

n_moves = 100;

for i = 1:n_moves
    
    pick = cups(2:4);
    cups(2:4) = [];
    
    dest = mod(cups(1) - 2, 9) + 1;
    while ~any(cups == dest)
        dest = mod(dest - 2, 9) + 1;
    end
    
    ind_dest = find(cups == dest);
    cups = [cups(1:ind_dest) pick cups(ind_dest+1:end)];

    cups = [cups(2:end) cups(1)];
    
end

ind_1 = find(cups == 1);
R = join(string([cups(ind_1+1:end) cups(1:ind_1-1)]), '')