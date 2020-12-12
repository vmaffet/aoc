fid = fopen('input.txt');
instructions = textscan(fid, '%c%f');
fclose(fid);

actions = instructions{1};
values  = instructions{2};

E = [ 1  0];
N = [ 0  1];
W = [-1  0];
S = [ 0 -1];

R = [0 -1
     1  0];
L = R^3; 

XY = [0 0];
F = E;

for k = 1:length(actions)

    a = actions(k);
    v = values(k);
    
    D = [0 0];
    T = eye(2);
    
    switch a
        case 'E'
            D = E;
        case 'N'
            D = N;
        case 'W'
            D = W;
        case 'S'
            D = S;
        case 'F'
            D = F;
        case 'R'
            T = R;
        case 'L'
            T = L;    
    end
    
    XY = XY + v*D;
    F = F*T^fix(v/90);
end

R = norm(XY, 1)