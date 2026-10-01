class TimeMap:

    from collections import defaultdict

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # binary search

        res = ''

        l = 0
        r = len(self.map[key]) - 1

        while l <= r:
            mid = (l + r) // 2
            v,t = self.map[key][mid]
            if t == timestamp:
                return v
            elif t < timestamp:
                res = v     # keep track of value of t < time
                l = mid + 1
            else:
                r = mid - 1
        
        return res
