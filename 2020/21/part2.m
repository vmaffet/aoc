foods = readtable('input.txt', 'ReadVariableNames',0, ...
                               'Delimiter',{'(contains',')'});

foods.Properties.VariableNames = {'ingredients', 'allergens'};

all_ingredients = join(foods.ingredients);
allergens = unique(split(join(foods.allergens, ', '), ', '));

foods.ingredients = cellfun(@split, foods.ingredients, 'UniformOutput', false);

candidates = cell(size(allergens));
for i = 1:length(allergens)
    pat = letterBoundary+allergens{i}+letterBoundary;
    in_food = contains(foods.allergens, pat);

    candidates{i} = func_n(@intersect, foods.ingredients{in_food});
end

matches = {};
while length(matches) < length(candidates)
    for i = 1:length(candidates)
        if numel(candidates{i}) > 1
            candidates{i} = setdiff(candidates{i}, matches);
        end
        if numel(candidates{i}) == 1
            matches = union(matches, candidates{i});
        end
    end
end

R = join([candidates{:}], ',')

function set = func_n(func, varargin)
    set = {};
    if length(varargin) == 1
        set = varargin{1};
    elseif length(varargin) > 1
        set = func(varargin{1}, func_n(func, varargin{2:end}));
    end
end