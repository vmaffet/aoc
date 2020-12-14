prog = readtable('input.txt', 'Format','%s %s', 'ReadVariableNames',0);

mask = '0';
mem = zeros(1, 'uint64');

for i = 1:height(prog)
    switch prog.Var1{i}
        case 'mask '
            mask = prog.Var2{i};
            
        otherwise
            idx = str2double(extract(prog.Var1{i}, digitsPattern));

            x = str2double(prog.Var2{i});
            x = bitand(x, bi2de(mask ~= '0', 'left-msb'), 'uint64');
            x = bitor(x,  bi2de(mask == '1', 'left-msb'), 'uint64');

            mem(idx) = x;
            
    end
end

R = sum(mem, 'native')