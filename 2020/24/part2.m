tiles = importdata('input.txt');

pat = lookBehindBoundary(lineBoundary|"e"|"w")+lookAheadBoundary("e"|"w");
tiles = replace(tiles, pat, "t");

dirs = {'te', 'ne',  'nw',  'tw', 'sw', 'se'};
vect = [1+0i, 0+1i, -1+1i, -1+0i, 0-1i, 1-1i];

dir_count = cellfun(@(d) count(tiles, d), dirs, 'UniformOutput', false);
dir_count = [dir_count{:}];

tile_pos = dir_count * vect';
tile_unq = unique(tile_pos);
tile_cnt = arrayfun(@(tp)sum(tile_pos == tp), tile_unq);

tile_unq = tile_unq(mod(tile_cnt, 2) == 1);

x = real(tile_unq) - min(real(tile_unq)) + 1;
y = imag(tile_unq) - min(imag(tile_unq)) + 1;

map = zeros(max(y), max(x), 'logical');
map(sub2ind(size(map), y, x)) = 1;

kernel = [1 1 0
          1 0 1
          0 1 1];

n_days = 100;
for d = 1:n_days

    map = padarray(map, [1,1], 0);
    neigh = conv2(map, kernel, 'same');

    map( map & neigh ~= 1) = 0;
    map(~map & neigh == 2) = 1;
    
end

R = sum(map, 'all')