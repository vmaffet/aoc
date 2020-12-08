rules = importdata('input.txt');

keyval = split(rules, ' bags contain ');

starts = keyval(:,1);
targets = regexp(keyval(:,2), '\d+ (\w+ \w+) bag', 'tokens');

G = digraph;
for i = 1:length(starts)
    start = starts{i};
    for j = 1:length(targets{i})
        target = targets{i}{j};
        G = addedge(G, start, target);
    end
end

H = flipedge(G);

bags = bfsearch(H, 'shiny gold');

R = length(bags) - 1


