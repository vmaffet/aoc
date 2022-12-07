input = importdata('input.txt');

history = cellfun(@split, input, 'UniformOutput',false);

s = [];
t = [];
w = dictionary("\", 0);
for i = 1:length(history)
    if history{i}{1} == '$'
        if history{i}{2} == 'cd'
            switch history{i}{3}
                case '/'
                    path = ["\"];
                case '..'
                    path = path(1:end-1);
                otherwise
                    path = [path, history{i}{3}];
            end
        end
    else
        from = string(fullfile(path{:}));
        to = fullfile(from, history{i}{2});
        s = [s, from];
        t = [t, to];
        if history{i}{1} == "dir"
            w(to) = 0;
        else
            w(to) = str2double(history{i}{1});
        end
    end
end

fs = digraph(s, t);

directories = fs.Nodes.Name(outdegree(fs) > 0);
for n = 1:length(directories)
    dir = directories(n);
    childs = bfsearch(fs, dir);
    w(dir) = sum(w(fs.Nodes.Name(childs)));
end

dir_weights = w(directories);

small_dirs = directories(dir_weights <= 100000);

part1 = sum(w(small_dirs))

free_space = 70000000 - w("\");
part2 = min(dir_weights(dir_weights > 30000000 - free_space))
