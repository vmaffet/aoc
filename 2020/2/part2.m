tbl = readtable('input.txt', 'ReadVariableNames',false, ...
                             'Delimiter',{' ','-',':'});
tbl.Properties.VariableNames = {'low','high','char','nan','pass'};

index = @(s, i) s(i);

char_low  = cellfun(index, tbl.pass, num2cell(tbl.low));
char_high = cellfun(index, tbl.pass, num2cell(tbl.high));

valid_low  = [tbl.char{:}]' == char_low;
valid_high = [tbl.char{:}]' == char_high;

valid = xor(valid_low, valid_high);

N = sum(valid)
