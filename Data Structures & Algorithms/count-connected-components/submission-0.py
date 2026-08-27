class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # start with each node being its own component
        # iterate through edges
        # make the connections -> decrease num components as you connect
        # return num components at the end

        result = n
        components = UnionFind(n)

        for a, b in edges:
            if components.find(a) != components.find(b):
                result -= 1
            components.union(a, b)

        return result



class UnionFind:
    def __init__(self, n: int):
        self.parent = {i: i for i in range(n)}
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        
        self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, a, b):
        p1 = self.find(self.parent[a])
        p2 = self.find(self.parent[b])

        self.parent[p1] = p2

        return