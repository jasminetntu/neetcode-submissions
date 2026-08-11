class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # we can only add ) if ( exists already
        # must start with (
        # 2 paths: add ( or )
        
        return self.findCombo(n, [], ['('], 1)

    def findCombo(self, nLeft, result, currCombo, currOpen):
        if nLeft == 0:
            result.append(''.join(currCombo))
        else:
            # print(nLeft, result, currCombo, currOpen)
            # add open
            if currOpen < nLeft:
                currCombo.append('(')
                self.findCombo(nLeft, result, currCombo, currOpen + 1)
                currCombo.pop()

            # add close
            if currOpen > 0:
                currCombo.append(')')
                self.findCombo(nLeft - 1, result, currCombo, currOpen - 1)
                currCombo.pop()

        return result