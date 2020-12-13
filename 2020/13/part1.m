fid = fopen('input.txt');
data = textscan(fid, '%f', 'Delimiter',',x', 'MultipleDelimsAsOne',1);
fclose(fid);

time  = data{1}(1);
buses = data{1}(2:end);

departs = fix(time./buses).*buses;
missed = departs < time;
departs(missed) = departs(missed) + buses(missed);

[earliest, idx] = min(departs);

R = (earliest-time)*buses(idx)
