class Solution:
    from collections import defaultdict

    def isAnagram(self, s: str, t: str) -> bool:
        sCounts = defaultdict(int)
        for c in s:
            sCounts[c] += 1
        
        for c in t:
            sCounts[c] -= 1
            if sCounts[c] < 0:
                return False
        
        if sum(sCounts.values()) != 0:
            return False
        return True
