class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k = the top _ of nums that appear most frequently
        # any order

        # k guaranteed > 1 and < unique(nums)
        
        # iterate through nums
        # count num appearances of each unique -> use dict
        # get the max k values

        from collections import defaultdict

        counts = defaultdict(int) # initializes everything added as an int

        for i in range(len(nums)): # count num appearances
            counts[nums[i]] += 1
        
        # get list of keys sorted descending by value
        sorted_counts = sorted(counts, key=counts.get, reverse=True) 

        result = sorted_counts[:k] # get first k

        # time complexity: O(n)
        
        return result

        