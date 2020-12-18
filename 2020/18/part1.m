operations = importdata('input.txt', '\n');

operations = replace(operations, digitBoundary('start'), 'N(');
operations = replace(operations, digitBoundary('end'), ')');

operations = replace(operations, '*', '-');

values = cellfun(@(s) uint64(eval(s)), operations);

R = sum(values, 'native')
