class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.nums)
        
        # self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappushpop(self.nums, val)
        
        # topk = heapq.nlargest(self.k, self.nums)
        # print(self.nums, val)
        return self.nums[0]

        # self.nums.append(val)
        # self.nums.sort(reverse=True)
        # return self.nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)