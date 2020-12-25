tiles = importdata('input.txt');

pat = lookBehindBoundary(lineBoundary|"e"|"w")+lookAheadBoundary("e"|"w");
tiles = replace(tiles, pat, "t");

dirs = {'te', 'ne', 'nw', 'tw', 'sw', 'se'};
vect = exp(1i*(0:5)*pi/3);

dir_count = cellfun(@(d) count(tiles, d), dirs, 'UniformOutput', false);
dir_count = [dir_count{:}];

tile_pos = round(dir_count * vect', 5);

tile_cnt = arrayfun(@(tp)sum(tile_pos == tp), unique(tile_pos));

R = sum(mod(tile_cnt, 2) == 1)
