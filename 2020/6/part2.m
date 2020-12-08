data = fileread('input.txt');

forms = split(data, compose({'\r\n\r\n', '\n\n', '\r\r'}));
forms = cellfun(@split, forms, 'UniformOutput', false);

common = cellfun(@(f) reduce(@intersect, f), forms, 'UniformOutput', false);

R = numel([common{:}])

function ret = reduce(func, cll)
    if size(cll, 1) > 1
        ret = func(cll{1}, reduce(func, cll(2:end)));
    else
        ret = cll{1};
    end
end