input = readtable('input.txt', 'ReadVariableNames', false);
strategy = renamevars(input, [1, 2], ["Player1", "Player2"]);

strategy.Score1 = cellfun(@rps1, strategy.Player1, strategy.Player2);
strategy.Score2 = cellfun(@rps2, strategy.Player1, strategy.Player2);

part1 = sum(strategy.Score1)
part2 = sum(strategy.Score2)

function score = rps1(a, b)
    shape_score = dictionary("X",1,"Y",2,"Z",3);
    outcome_score = dictionary(...
        ["AZ","BX","CY"], 0,...
        ["AX","BY","CZ"], 3,...
        ["AY","BZ","CX"], 6);

    score = shape_score(b) + outcome_score(strcat(a, b));
end

function score = rps2(a, b)
    outcome_score = dictionary("X",0,"Y",3,"Z",6);
    shape_score = dictionary(...
        ["AY","BX","CZ"],1,...
        ["AZ","BY","CX"],2,...
        ["AX","BZ","CY"],3);

    score = shape_score(strcat(a, b)) + outcome_score(b);
end
