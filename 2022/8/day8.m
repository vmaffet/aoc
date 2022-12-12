forest = char(splitlines(fileread('input.txt'))) - '0';

S = cummax(forest, 1, "forward");
N = cummax(forest, 1, "reverse");
E = cummax(forest, 2, "forward");
W = cummax(forest, 2, "reverse");

S = S(1:end-2, 2:end-1);
N = N(3:end, 2:end-1);
E = E(2:end-1, 1:end-2);
W = W(2:end-1, 3:end);

treeline = padarray(min(cat(3, S, N, E, W), [], 3), [1, 1], -1);

part1 = sum(treeline < forest, 'all')

part2 = max(arrayfun(@(idx) scenic(forest, idx), 1:numel(forest)))

function score = scenic(forest, idx)

    [y, x] = ind2sub(size(forest), idx);
    t = forest(y, x);

    s = cummax(forest(y+1:end, x)) < t;
    n = cummax(forest(y-1:-1:1, x)) < t;
    e = cummax(forest(y, x+1:end)) < t;
    w = cummax(forest(y, x-1:-1:1)) < t;

    score = prod(cellfun(@(c) sum(c) + ismember(0, c), {s, n, e, w}));
end
