input_file = 'input.txt';
fields = readtable(input_file, 'Delimiter',{': ','-',' or '}, ...
                               'ReadVariableNames',0, ...
                               'CommentStyle',{'your ticket:','$'});

rng = num2str(height(fields)+3);
my_ticket = readmatrix(input_file, 'Range',[rng ':' rng]);
                           
tickets = readmatrix(input_file, 'NumHeaderLines',height(fields)+5);

field_valid = zeros(height(fields), max(tickets, [], 'all'), 'logical');
for k = 1:height(fields)
    field_valid(k, [fields{k,2}:fields{k,3} fields{k,4}:fields{k,5}]) = 1;
end

valid = any(field_valid);
good_tickets = all(valid(tickets), 2);
tickets = tickets(good_tickets, :);

matching = zeros(height(fields), size(tickets, 2), 'logical');
for k = 1:size(matching, 1)
    for j = 1:size(matching, 2)
        matching(k,j) = all(field_valid(k, tickets(:,j)));
    end
end

field_to_idx = zeros(height(fields), 1);
for k = 1:height(fields)
    i = find(sum(matching) == 1, 1);
    f = find(matching(:,i));
    field_to_idx(f) = i;
    matching(f, :) = 0;
end

departure_fields = startsWith(fields.Var1, 'departure');
values = my_ticket(field_to_idx(departure_fields));

R = uint64(prod(values))