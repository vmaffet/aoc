decks = readmatrix('input.txt');

sep = find(isnan(decks));

player1 = decks(1:sep-1)';
player2 = decks(sep+1:end)';

[~, winning_deck] = combat(player1, player2);

R = conv(winning_deck, 1:numel(winning_deck), 'valid')

function [win_p1, win_deck] = combat(deck1, deck2)
    seen_deck1 = {deck1};
    seen_deck2 = {deck2};
    
    while numel(deck1) && numel(deck2)
        
        card1 = deck1(1);
        card2 = deck2(1);

        deck1(1) = [];
        deck2(1) = [];
        
        if numel(deck1) < card1 || numel(deck2) < card2
            p1_wins = card1 > card2;
        else
            [p1_wins, ~] = combat(deck1(1:card1), deck2(1:card2));
        end

        if p1_wins
            deck1(end+1:end+2) = [card1 card2];
        else
            deck2(end+1:end+2) = [card2 card1];
        end
        
        dup1 = cellfun(@(d)isequal(d, deck1), seen_deck1);
        dup2 = cellfun(@(d)isequal(d, deck2), seen_deck2);
        if any(dup1 & dup2)
            deck2 = [];
        end
        
        seen_deck1{end+1} = deck1;
        seen_deck2{end+1} = deck2;
    end
    
    win_p1 = numel(deck1) > 0;
    if win_p1
        win_deck = deck1;
    else
        win_deck = deck2;
    end
end
