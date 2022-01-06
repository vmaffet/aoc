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

    candidates{i} = fold(@intersect, foods.ingredients(in_food));
end

has_allergen = fold(@union, candidates);
non_allergen = strtrim(erase(all_ingredients, has_allergen));

R = length(split(non_allergen))