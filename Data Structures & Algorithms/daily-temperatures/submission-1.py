class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        output = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                stack_value, stack_index = stack.pop()
                output[stack_index] = (i - stack_index)
            stack.append([v, i])
        return output


        # temperatures = [30,38,30,36,35,40,28]
        # output = [[], [], [], []]
        # stack = [[], [], []]
        