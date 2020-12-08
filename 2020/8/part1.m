program = readtable('input.txt');
program.Properties.VariableNames = {'Operation', 'Argument'};
program.Operation = categorical(program.Operation);

program.Executed = false(height(program),1);
accumulator = 0;
instr = 1;

while instr > 0 && instr <= height(program) && ~program.Executed(instr) 
    
    program.Executed(instr) = true;
    
    switch program.Operation(instr)
        case 'acc'
            accumulator = accumulator + program.Argument(instr);
            instr = instr + 1;
        case 'jmp'
            instr = instr + program.Argument(instr);
        case 'nop'
            instr = instr + 1;
        otherwise
    end
end

R = accumulator