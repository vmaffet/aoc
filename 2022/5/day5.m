input = splitlines(fileread('input.txt'));

sep = find(strcmp(input, char));

crates = char(input(1:sep-2));
crates = cellstr(crates(end:-1:1, 2:4:size(crates, 2))');

process = string(input(sep+1:end));

part1 = rearrange(process, crates, true)
part2 = rearrange(process, crates, false)

function top = rearrange(process, crates, singlemode)
    for i = 1:length(process)
        nab = double(extract(process(i), digitsPattern));
        
        s = crates{nab(2)}(end-nab(1)+1:end);
        crates{nab(2)}(end-nab(1)+1:end) = [];
        if singlemode
            s = reverse(s);
        end
        crates{nab(3)} = [crates{nab(3)}, s];
    end
    top = char(extract(crates, lettersPattern(1)+lineBoundary))';
end
