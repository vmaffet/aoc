prog = readtable('input.txt', 'Format','%s %s', 'ReadVariableNames',0);

mem = containers.Map('KeyType','uint64','ValueType','uint64');

for i = 1:height(prog)
    switch prog.Var1{i}
        case 'mask '
            mask = prog.Var2{i};
            floating = mask == 'X';
            variations = de2bi(0:(2^sum(floating)-1));

        otherwise
            idx = str2double(extract(prog.Var1{i}, digitsPattern));
            idx = bitor(de2bi(idx, 36, 'left-msb'), mask == '1');
            
            x = str2double(prog.Var2{i});

            for k = 1:size(variations, 1)
                idx(floating) = variations(k, :);
                mem(bi2de(idx, 'left-msb')) = x;
            end
    end
end

R = sum(cell2mat(values(mem)), 'native')