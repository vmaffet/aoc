data = fileread('input.txt');

passports = split(data, compose({'\r\n\r\n', '\n\n', '\r\r'}));
passports = replace(passports, compose({'\r\n', '\n', '\r'}), ' ');

regexps = {'byr:(19[2-9]\d|200[0-2])\>', ...
           'iyr:20(1\d|20)\>', ...
           'eyr:20(2\d|30)\>', ...
           'hgt:(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)\>', ...
           'hcl:#[0-9a-f]{6}\>', ...
           'ecl:(amb|blu|brn|gry|grn|hzl|oth)\>', ...
           'pid:\d{9}\>'};

pass_contains = @(rgx) contains(passports, regexpPattern(rgx));
valid_field = cellfun(pass_contains, regexps, 'UniformOutput', false);

valid_pass = all([valid_field{:}], 2);

R = sum(valid_pass)
