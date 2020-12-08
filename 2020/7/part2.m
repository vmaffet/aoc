rules = importdata('input.txt');

keyval = split(rules, ' bags contain ');

starts = keyval(:,1);
targets = regexp(keyval(:,2), '(\d+) (\w+ \w+) bag', 'tokens');

G = digraph;
for i = 1:length(keyval)
    start = starts{i};
    for j = 1:length(targets{i})
        target = targets{i}{j}{2};
        weight = str2double(targets{i}{j}{1});
        G = addedge(G, start, target, weight);
    end
end

R = childrens(G, 'shiny gold')

function C = childrens(G, s)
    C = 0;
    [eid, tid] = outedges(G, s);
    for i = 1:length(eid)
        w = G.Edges.Weight(eid(i));
        C = C + w + w*childrens(G, tid{i});
    end
end
