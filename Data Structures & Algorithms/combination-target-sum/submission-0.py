class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def findCombinations(candidate_idx, currCandidates, currSum):
            nonlocal result
            
            if currSum > target or candidate_idx >= len(candidates):
                return
            if currSum == target:
                result.append(currCandidates.copy())
                return
            
            # take curr candidate
            currCandidates.append(candidates[candidate_idx])
            findCombinations(candidate_idx, currCandidates, currSum + candidates[candidate_idx])
            currCandidates.pop() # undo

            # skip curr candidate
            findCombinations(candidate_idx + 1, currCandidates, currSum)
            
            return

        findCombinations(0, [], 0)
        return result