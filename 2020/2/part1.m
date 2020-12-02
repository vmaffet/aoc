tbl = readtable('input.txt', 'ReadVariableNames',false, ...
                             'Delimiter',{' ','-',':'});
tbl.Properties.VariableNames = {'low','high','char','nan','pass'};

cnts = cellfun(@count, tbl.pass, tbl.char);

valid = tbl.low <= cnts & cnts <= tbl.high;

N = sum(valid)
