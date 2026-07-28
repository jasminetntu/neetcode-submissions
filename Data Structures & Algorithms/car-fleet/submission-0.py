class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sorted dec
        # add to stack
        # (1, 10)
        # (1, 8) -> matches or is lower than (1, 10), so don't add to stack
        # (7, 5)
        # (3, 3) -> < (7, 5), so don't add
        # (12, 0) -> > (7, 5), add
        # return len of stack

        sorted_pos = []
        for i in range(len(position)):
            sorted_pos.append((position[i], speed[i]))
        sorted_pos.sort(reverse=True) # sort by positions dec

        fleets = []

        for i in range(len(sorted_pos)):
            # calc time
            time = (target - sorted_pos[i][0]) / sorted_pos[i][1]

            # add to fleets
            if len(fleets) == 0:
                fleets.append(time)
            elif time > fleets[-1]:
                fleets.append(time)

        return len(fleets)
