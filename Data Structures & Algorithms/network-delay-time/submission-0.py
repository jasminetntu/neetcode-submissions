class Solution:
    from collections import defaultdict
    import heapq

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # djikstras algo

        # start at node k
        # keep track of time
        # choose the min edge & mark node as visited
        # continue pattern with that node
        # if that node has no where else to go, backtrack
        # go to next min edge -> mark node as visited ONLY IF it is not visited yet
        # repeat
        # if all nodes received signal, return time
        # otherwise return -1


        # make graph of edges
        edges = defaultdict(list)
        for source, target, time in times:
            edges[source].append((target, time))

        minTimes = [-1] * (n + 1)
        minTimes[0], minTimes[k] = 0, 0

        heap = [(0, k)]
        heapq.heapify(heap)

        while len(heap):
            t, curr = heapq.heappop(heap)

            if t <= minTimes[curr]:
                for target, time in edges[curr]:
                    newTime = t + time
                    if minTimes[target] == -1 or newTime < minTimes[target]:
                        minTimes[target] = newTime
                        heapq.heappush(heap, (minTimes[target], target))

        if -1 not in minTimes:
            return max(minTimes)
        return -1