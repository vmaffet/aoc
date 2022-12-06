input = string(importdata('input.txt'));

pairs = double(split(input, [",","-"]));
A1 = pairs(:,1);
A2 = pairs(:,2);
B1 = pairs(:,3);
B2 = pairs(:,4);

part1 = sum(contains(A1, A2, B1, B2))
part2 = sum(overlaps(A1, A2, B1, B2))

function tf = contains(a1, a2, b1, b2)
    a_in_b = b1 <= a1 & a2 <= b2;
    b_in_a = a1 <= b1 & b2 <= a2;
    tf = a_in_b | b_in_a;
end

function tf = overlaps(a1, a2, b1, b2)
    a1_in_b = b1 <= a1 & a1 <= b2;
    a2_in_b = b1 <= a2 & a2 <= b2;
    tf = a1_in_b | a2_in_b | contains(a1, a2, b1, b2);
end