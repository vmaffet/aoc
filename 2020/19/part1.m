data = importdata('input.txt', '\n');

is_rule = contains(data, ':');

rules = data(is_rule);
messages = data(~is_rule);

rules = erase(rules, '"');
rules = replace(rules, digitBoundary('start'), 'rgx');
rules = replace(rules, ' rgx', ' (??@rgx');
rules = replace(rules, digitBoundary('end')+(' '|lineBoundary('end')), ') ');
rules = replace(rules, ':', '=''');
rules = append(rules, ''';');
rules = erase(rules, ' ');

cellfun(@eval, rules);

matches = regexp(messages, ['^' rgx0 '$']);

R = sum([matches{:}])