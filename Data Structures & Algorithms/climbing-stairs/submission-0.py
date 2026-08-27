class Solution:
    from collections import defaultdict
    
    def climbStairs(self, n: int) -> int:
        # only 2 paths: 1 or 2 for each pair of stairs
        # basically finding all the ways to split n into groups of 1 & 2

        return self.climb(n, defaultdict(int))

    
    def climb(self, n, mem):
        if n in mem:
            return mem[n]
        if n == 0 or n == 1:
            return 1
        
        # take 1 step + take 2 steps
        # store in dict
        mem[n] = self.climb(n - 1, mem) + self.climb(n - 2, mem)

        return mem[n]