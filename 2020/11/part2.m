boat = cell2mat(importdata('input.txt'));

seats = boat == 'L';

boat = zeros(size(boat));
boat(seats) = -1;

[H, W] = size(boat);
D = min(size(boat));

kernel_E  = zeros(2*W-1);
kernel_SE = zeros(2*D-1);
kernel_S  = zeros(2*H-1);

kernel_E(W, W+1:end) = 2.^-(1:W-1);
kernel_SE(eye(2*D-1, 'logical')) = [zeros(1,D) 2.^-(1:D-1)];
kernel_S(H+1:end, H) = 2.^-(1:H-1);

kernel_SW = kernel_SE(:, end:-1:1);
kernel_W  = kernel_E(:, end:-1:1);
kernel_NW = kernel_SE(end:-1:1, end:-1:1);
kernel_N  = kernel_S(end:-1:1, :);
kernel_NE = kernel_SE(end:-1:1, :);

prev = boat - 1;
while ~isequal(prev, boat)
    prev = boat;
    
    adjacent_W  = conv2(boat, kernel_E,  'same') > 0;
    adjacent_NW = conv2(boat, kernel_SE, 'same') > 0;
    adjacent_N  = conv2(boat, kernel_S,  'same') > 0;
    adjacent_NE = conv2(boat, kernel_SW, 'same') > 0;
    adjacent_E  = conv2(boat, kernel_W,  'same') > 0;
    adjacent_SE = conv2(boat, kernel_NW, 'same') > 0;
    adjacent_S  = conv2(boat, kernel_N,  'same') > 0;
    adjacent_SW = conv2(boat, kernel_NE, 'same') > 0;
    
    adjacent = adjacent_W + adjacent_NW + adjacent_N + adjacent_NE + ...
               adjacent_E + adjacent_SE + adjacent_S + adjacent_SW;

    boat(adjacent == 0) = 1;
    boat(adjacent >= 5) = -1;
    boat(~seats) = 0;
end
      
R = sum(boat > 0, 'all')

