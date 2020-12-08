data = fileread('input.txt');

forms = split(data, compose({'\r\n\r\n', '\n\n', '\r\r'}));
forms = replace(forms, compose({'\r\n', '\n', '\r'}), '');

combined = cellfun(@unique, forms, 'UniformOutput',false);

R = numel([combined{:}])