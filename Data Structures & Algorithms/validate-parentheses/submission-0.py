class Solution:
    def isValid(self, s: str) -> bool:
        # stack -> keep track of what weve seen
        # iterate through string
        # if curr closed top of stack -> remove from stack 
        # if curr = wrong closing for top -> return False
        # by the end, if stack !empty -> return False
        # else return True

        # always pop

        seen = []
        
        for i in range(len(s)):
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if len(seen) == 0:
                    return False
                else:
                    last = seen.pop(-1)
                
                if (s[i] == ')' and last != '(') or (s[i] == '}' and last != '{') or (s[i] == ']' and last != '['):
                    return False
            else:
                seen.append(s[i])
        
        if len(seen) != 0:
            return False
        
        return True
                
            