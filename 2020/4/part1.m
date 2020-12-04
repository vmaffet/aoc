data = fileread('input.txt');

passports = split(data, compose('\n\n'));
passports = replace(passports, compose('\n'), ' ');

fields = {'byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:'};

pass_contains = @(key) contains(passports, key);
field_in = cellfun(pass_contains, fields, 'UniformOutput', false);

valid_pass = all([field_in{:}], 2);

R = sum(valid_pass)
