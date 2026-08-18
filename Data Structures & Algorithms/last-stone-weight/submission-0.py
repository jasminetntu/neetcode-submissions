class Solution:
    import heapq

    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): # max heap
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1

            if x < y:
                heapq.heappush(stones, (y - x) * -1)
        

        if len(stones) == 0:
            return 0
        return stones[0] * -1


        