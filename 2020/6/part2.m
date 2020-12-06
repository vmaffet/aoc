data = fileread('input.txt');

forms = split(data, compose('\n\n'));
sep_group = @(s) split(s, compose('\n'));
forms = cellfun(sep_group, forms, 'UniformOutput', false);

common = cellfun(@(f) reduce(@intersect, f), forms, 'UniformOutput', false);

R = numel([common{:}])

function ret = reduce(func, cll)

    if size(cll, 1) > 1
        ret = func(cll{1}, reduce(func, cll(2:end)));
    else
        ret = cll{1};
    end

end