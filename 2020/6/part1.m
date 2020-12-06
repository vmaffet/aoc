data = fileread('input.txt');

forms = split(data, compose('\n\n'));
forms = replace(forms, compose('\n'), '');

combined = cellfun(@unique, forms, 'UniformOutput',false);

R = numel([combined{:}])