input_file = 'input.txt';
fields = readtable(input_file, 'Delimiter',{': ','-',' or '}, ...
                               'ReadVariableNames',0, ...
                               'CommentStyle',{'your ticket:','$'});

tickets = readmatrix(input_file, 'NumHeaderLines',height(fields)+5);

valid = zeros(max(tickets, [], 'all'), 1, 'logical');
for k = 1:height(fields)
    valid([fields{k,2}:fields{k,3} fields{k,4}:fields{k,5}]) = 1;
end

invalid = tickets(~valid(tickets));

R = sum(invalid)