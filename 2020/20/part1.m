function [out_tile, out_trans] = part1
    data = importdata('input.txt');

    is_desc = contains(data, 'Tile');

    n_tiles = sum(is_desc);

    id = uint64(str2double(extract(data(is_desc), digitsPattern)));

    tiles = cell2mat(data(~is_desc)) == '#';
    tiles = reshape(tiles', size(tiles, 2), [], n_tiles);

    %1:R0 2:MX 3:MY 4:R180 5:R90 6:TM 7:TA 8:R270
    n_trans = 8;
    
    img_tile  = zeros(sqrt(n_tiles));
    img_trans = n_trans * ones(sqrt(n_tiles)); 
    
    img_idx = 1;
    img_size = size(img_tile);
    while img_idx <= n_tiles
        [row, col] = ind2sub(img_size, img_idx);
        
        match = true;
        
        img_trans(row, col) = img_trans(row, col) + 1;
        if img_trans(row, col) > n_trans
           if any(img_tile == img_tile(row, col) + 1, 'all') || img_tile(row, col) == n_tiles
               match = false;
           else
               img_trans(row, col) = 1;
           end
           
           img_tile(row, col)  = img_tile(row, col) + 1;
        end
        
        idx_tile = img_tile(row, col);
        idx_trans = img_trans(row, col);
        
        if match && row > 1
            neigh_tile = img_tile(row-1, col);
            neigh_trans = img_trans(row-1, col);
            match = all(get_edge(idx_tile,   'north', idx_trans) == ...
                        get_edge(neigh_tile, 'south', neigh_trans));
        end

        if match && col > 1
            neigh_tile = img_tile(row, col-1);
            neigh_trans = img_trans(row, col-1);
            match = all(get_edge(idx_tile,   'west', idx_trans) == ...
                        get_edge(neigh_tile, 'east', neigh_trans));
        end
        
        if match
           img_idx = img_idx + 1;
        elseif img_tile(row, col) >= n_tiles && img_trans(row, col) >= n_trans
           img_tile(row, col)  = 0;
           img_trans(row, col) = n_trans;
           img_idx = img_idx - 1;
        end
    end
    
    R = prod(id([img_tile(1,1), img_tile(end,1), ...
                 img_tile(1,end), img_tile(end,end)]), 'native')
             
    if nargout == 2
        out_tile = img_tile;
        out_trans = img_trans;
    end
    
    function arr = get_edge(tile_id, edge, trans_id)
        tile = tiles(:, :, tile_id);
        switch [48+trans_id ':' edge]
            case {'1:north', '3:south', '6:west', '8:east'}
                arr = tile(1, :);
            case {'3:north', '1:south', '8:west', '6:east'}
                arr = tile(end, :);
            case {'6:north', '5:south', '1:west', '2:east'}
                arr = tile(:, 1)';
            case {'5:north', '6:south', '2:west', '1:east'}
                arr = tile(:, end)';
            case {'2:north', '4:south', '5:west', '7:east'}
                arr = tile(1, end:-1:1);
            case {'4:north', '2:south', '7:west', '5:east'}
                arr = tile(end, end:-1:1);
            case {'8:north', '7:south', '3:west', '4:east'}
                arr = tile(end:-1:1, 1)';
            case {'7:north', '8:south', '4:west', '3:east'}
                arr = tile(end:-1:1, end)';
        end
    end
end
