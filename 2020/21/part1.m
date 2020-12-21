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

has_allergen = func_n(@union, candidates{:});
non_allergen = strtrim(erase(all_ingredients, has_allergen));

R = length(split(non_allergen))

function set = func_n(func, varargin)
    set = {};
    if length(varargin) == 1
        set = varargin{1};
    elseif length(varargin) > 1
        set = func(varargin{1}, func_n(func, varargin{2:end}));
    end
end