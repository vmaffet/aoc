data = split(fileread('input.txt'));
constraints = textscan(replace(data{2}, 'x', '1'), '%d64', 'Delimiter',',');
constraints = constraints{1};

trivial = constraints == 1;

% Chinese remainder theorem
ni = constraints(~trivial);
ai = -int64(find(~trivial)-1);

n = prod(ni, 'native');
ni_hat = n./ni;

[gi,ui,vi] = gcd(ni, ni_hat);

ei = vi.*ni_hat;

R = mod(sum(ai.*ei, 'native'), n)
