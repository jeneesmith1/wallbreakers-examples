        #N = (N - 1) + (N - 2)
        # sum +
        
        #F(0) = 0
        #F(1) = 1
        #F(2) = F(1) + F(0) = 1 + 0
        #F(3) = F(2) + F(1) = 1 + 1 = 2
        #F(4) = F(3) + F(2) = 2 + 1 = 3
class Solution:     
    def fibRecursive(self, N:int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)
    
    def fibIterative(self, N: int) -> int:
        curr_sum = 0
        prev_sum = 1
        prev_prev_sum = 0
        
        if N == 0:
            curr_sum += 0
            return 0
        if N == 1:
            curr_sum += 1
            return 1
        else:
            for i in range(2, N+ 1):
                curr_sum = prev_sum + prev_prev_sum
                prev_prev_sum = prev_sum
                prev_sum = curr_sum
            
            return curr_sum
                
                
                
        