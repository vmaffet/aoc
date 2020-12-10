adapters = readmatrix('input.txt');
adapters = sort(adapters);

arrngmnts = zeros(adapters(end)+3, 1, 'uint64');
arrngmnts(3) = 1;

for jolt = adapters'
    arrngmnts(jolt+3) = sum(arrngmnts([jolt jolt+1 jolt+2]));
end

R = arrngmnts(end)