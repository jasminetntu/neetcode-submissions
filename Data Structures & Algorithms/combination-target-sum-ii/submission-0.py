class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sortedCandidates = sorted(candidates)
        # print(sortedCandidates)
        return self.findCombination(sortedCandidates, target, [], 0, [], 0)
    
    def findCombination(self, candidates, target, result, candidateIdx, currCandidates, currSum):
        # print(result, candidateIdx, currCandidates, currSum)
        if currSum == target and currCandidates not in result:
            result.append(currCandidates.copy())
            return
        
        if currSum > target or candidateIdx >= len(candidates):
            return
        
        # take curr idx
        currCandidates.append(candidates[candidateIdx])
        self.findCombination(candidates, target, result, candidateIdx + 1, currCandidates, currSum + candidates[candidateIdx])
        currCandidates.pop() # undo choice

        # skip curr idx
        while candidateIdx < len(candidates) - 1 and candidates[candidateIdx + 1] == candidates[candidateIdx]:
            candidateIdx += 1
        
        self.findCombination(candidates, target, result, candidateIdx + 1, currCandidates, currSum)

        return result
            