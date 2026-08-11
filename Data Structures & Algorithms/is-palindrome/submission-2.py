class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 ptr
        # go from both ends of parsed string (lowercase, no space, no punctuation)
        # as soon as something doesnt
        
        ps = s.replace(' ', '').lower() # parse string
        
        i = 0
        j = len(ps) - 1
        
        while i < j:
            # print(ps[i], ps[j])
            if not (0 <= ord(ps[i]) - ord('a') <= 25 or 0 <= ord(ps[i]) - ord('0') <= 9): # not a lowercase letter or number, then skip
                i += 1
            elif not (0 <= ord(ps[j]) - ord('a') <= 25 or 0 <= ord(ps[j]) - ord('0') <= 9):
                j -= 1
            else: 
                if ps[i] != ps[j]:
                    return False
                else:
                    i += 1
                    j -= 1
        return True
        
        