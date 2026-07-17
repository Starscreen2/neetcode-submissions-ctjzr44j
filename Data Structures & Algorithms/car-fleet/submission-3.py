class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = [[p, s] for p, s in sorted(zip(position, speed))]

        stack = []

        for p, s in (temp)[::-1]:
            time = ((target - p) / s)
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
                



# position = [4,1,0,7], speed = [2,2,1,1]
# position = [0,1,4,7], speed = [1,2,2,1] sorted

# target - position / speed = time
# stack = [[], [], [], [], []]
# answer = []