decks = readmatrix('input.txt');

sep = find(isnan(decks));

player1 = decks(1:sep-1);
player2 = decks(sep+1:end);

while numel(player1) && numel(player2)

    card1 = player1(1);
    card2 = player2(1);
    
    player1(1) = [];
    player2(1) = [];
    
    if card1 > card2
        player1(end+1:end+2) = [card1 card2];
    else
        player2(end+1:end+2) = [card2 card1];
    end
    
end

if numel(player1)
    winner = player1;
else
    winner = player2;
end

R = conv(winner, 1:numel(winner), 'valid')