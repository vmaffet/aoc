classdef N
   properties
      val {mustBeNumeric}
   end
   methods
      function obj = N(val)
         obj.val = val;
      end
      function u = uint64(obj)
         u = uint64(obj.val);
      end
      function r = plus(a,b)
         r = N(a.val + b.val);
      end
      function r = minus(a,b)
         r = N(a.val * b.val);
      end
      function r = mtimes(a,b)
         r = plus(a,b);
      end
   end
end