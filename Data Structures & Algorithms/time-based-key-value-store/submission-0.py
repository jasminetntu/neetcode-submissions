class TimeMap:

    from collections import defaultdict

    def __init__(self):
        self.map = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        for i in range(timestamp, -1, -1):
            if i in self.map[key]:
                return self.map[key][i]

        return ''