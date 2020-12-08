data = fileread('input.txt');

passports = split(data, compose({'\r\n\r\n', '\n\n', '\r\r'}));
passports = replace(passports, compose({'\r\n', '\n', '\r'}), ' ');

fields = {'byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:'};

pass_contains = @(key) contains(passports, key);
field_in = cellfun(pass_contains, fields, 'UniformOutput', false);

valid_pass = all([field_in{:}], 2);

R = sum(valid_pass)
