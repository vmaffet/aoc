boat = cell2mat(importdata('input.txt'));

seats = boat == 'L';

boat = zeros(size(boat));

kernel = [1 1 1
          1 0 1
          1 1 1];

prev = boat - 1;
while ~isequal(prev, boat)
    prev = boat;
    
    adjacent = conv2(boat, kernel, 'same');

    boat(adjacent == 0) = 1;
    boat(adjacent >= 4) = 0;
    boat(~seats) = 0;
end
      
R = sum(boat, 'all')

