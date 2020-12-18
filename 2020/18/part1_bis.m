function part1_bis
    operations = importdata('input.txt', '\n');

    values = cellfun(@opeval, operations);

    R = sum(values, 'native')
    
    function x = opeval(s)
        
        par_match = '\(([^()]|(??@par_match))*\)';
        pars = regexp(s, par_match, 'match');
        
        for i = 1:length(pars)
            sub = pars{i};
            s = replace(s, sub, num2str(opeval(sub(2:end-1))));
        end
        
        tokens = split(s, digitBoundary('end'));
        
        pre = repmat('(', 1, length(tokens)-1);
        post = join(tokens, ')');
        
        x = uint64(eval([pre post{1}]));
    
    end
end
