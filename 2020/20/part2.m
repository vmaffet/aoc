function part2
    data = importdata('input.txt');

    is_desc = contains(data, 'Tile');

    n_tiles = sum(is_desc);

    tiles = cell2mat(data(~is_desc)) == '#';
    tiles = reshape(tiles', size(tiles, 2), [], n_tiles);

    [idx_tiles, idx_trans] = part1;
    
    tiles = tiles(2:end-1, 2:end-1, :);
    
    for i = 1:n_tiles
        [row, col] = ind2sub(size(idx_trans), i);
        
        tile_idx = idx_tiles(row, col);
        trans_idx = idx_trans(row, col);
        tiles(:, :, tile_idx) = transform(tiles(:, :, tile_idx), trans_idx);
    end
    
    image = cell2mat(arrayfun(@(i)tiles(:,:,i), idx_tiles, 'UniformOutput', false))';
    
    monster = ['                  # '
               '#    ##    ##    ###'
               ' #  #  #  #  #  #   '] == '#';

    monster_size = sum(monster, 'all');
           
    for i = 1:8
        fmonster = transform(monster, i);
        cnt = sum(conv2(image, fmonster) == monster_size, 'all');
        if cnt ~= 0
            R = sum(image, 'all') - cnt * monster_size
        end
    end
    
    %1:R0 2:MX 3:MY 4:R180 5:R90 6:TM 7:TA 8:R270
    function tile = transform(tile, trans_id)
        switch trans_id
            case 1
            case 2
                tile = tile(:, end:-1:1);
            case 3
                tile = tile(end:-1:1, :);
            case 4
                tile = tile(end:-1:1, end:-1:1);
            case 5
                tile = tile(:, end:-1:1)';
            case 6
                tile = tile';
            case 7
                tile = tile(end:-1:1, end:-1:1)';
            case 8
                tile = tile(end:-1:1, :)';
        end
    end
end
