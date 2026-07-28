class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max k = max of piles
        # min k = 1

        high = max(piles)
        low = 1
        res = high

        while low < high:
            mid = (high + low) // 2

            num_hours = 0
            for i in range(len(piles)): # check if eats all
                num_hours += math.ceil(piles[i] / mid)
            if num_hours <= h: # if yes -> dec max
                res = mid
                high = mid
            else: # if not -> inc min
                low = mid + 1

        return res