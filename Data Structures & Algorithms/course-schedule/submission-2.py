class Solution:
    from collections import defaultdict, deque

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # create graph
        numPre = [0] * numCourses # keep track of prereqs
        pre = defaultdict(list) # key = prereq, value = list of courses
        for p in prerequisites:
            pre[p[1]].append(p[0]) 
            numPre[p[0]] += 1
        
        queue = deque()

        # start with courses with no prereqs
        for i in range(numCourses):
            if numPre[i] == 0:
                queue.append(i)
        
        while len(queue):
            c = queue.popleft()
            for course in pre[c]:
                numPre[course] -= 1
                if numPre[course] == 0:
                    queue.append(course) # append once we unlock course
        
        if sum(numPre) == 0:
            return True
        return False




# class Solution:
#     from collections import defaultdict

#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

#         # false if there is a loop/cycle somewhere -> prereq not possible
        
#         # loop through prereqs -> keep track of seen so far
#         # if one of the prereqs is ever in seen then its not possible
#         # once we complete 1 course & its complete prereqs, we can remove it from the list?
#         # build upon 1 list of prereqs?

#         if len(prerequisites) == 0:
#             return True

#         # make graph
#         pre = defaultdict(list)
#         for p in prerequisites:
#             pre[p[0]].append(p[1])
        
#         visited = set()
#         for c in range(numCourses):
#             if c not in visited:
#                 if self.findCycle(pre, c, set([c]), visited):
#                     return False

#         return True
    
#     def findCycle(self, pre, curr, seen, visited):        
#         for p in pre.get(curr, []):
#             if p not in visited:
#                 if p in seen:
#                     return True
                
#                 seen.add(p)
#                 if self.findCycle(pre, p, seen, visited):
#                     return True
#                 seen.remove(p) # undo append
        
#         visited.add(curr)
#         return False
        


#     # def findCycle(self, pre, result, seen):
#     #     for i in range(len(prereqs)):
#     #         if prereqs[i][0] == result[-1]:
#     #             if prereqs[i][1] in seen:
#     #                 return True
#     #             result.append(prereqs[i][1])
#     #             seen.append(prereqs[i][1])
#     #             return self.findCycle(prereqs, result, seen)
#     #     return False
        
