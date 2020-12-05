passes = importdata('input.txt');

passes_bin = replace(passes, "F"|"L", '0');
passes_bin = replace(passes_bin, "B"|"R", '1');

seat_ID = bin2dec(passes_bin);

R = max(seat_ID)