data = fileread('input.txt');

forms = split(data, compose({'\r\n\r\n', '\n\n', '\r\r'}));
forms = cellfun(@split, forms, 'UniformOutput', false);

common = cellfun(@(f) fold(@intersect, f), forms, 'UniformOutput', false);

R = numel([common{:}])