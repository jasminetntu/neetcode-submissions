class Solution:
    from collections import defaultdict, deque

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # make graph
        numPre = [0] * numCourses
        pre = defaultdict(list)
        for p in prerequisites:
            pre[p[1]].append(p[0])
            numPre[p[0]] += 1

        result = []
        queue = deque()

        # start w/ courses w/ no prereqs
        for course in range(numCourses):
            if numPre[course] == 0:
                queue.append(course)
        
        while len(queue):
            c = queue.popleft()
            result.append(c)

            for course in pre[c]:
                numPre[course] -= 1
                if numPre[course] == 0:
                    queue.append(course)

        if sum(numPre) == 0:
            return result
        return []