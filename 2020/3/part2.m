function part2

    M = cell2mat(importdata('input.txt'));
    [height, width] = size(M);

    rights = {1 3 5 7 1};
    downs  = {1 1 1 1 2};

    tree_counts = cellfun(@nb_trees, rights, downs);

    R = uint64(prod(tree_counts))

    function nt = nb_trees(r, d)
        down = 1:d:height;
        N = length(down);
        right = linspace(1, 1+r*(N-1), N);

        ind = sub2ind(size(M), down, mod(right-1, width) + 1);

        locations = M(ind);
        nt = count(locations, '#');
    end
end