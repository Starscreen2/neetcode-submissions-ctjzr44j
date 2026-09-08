class Solution:
    def climbStairs(self, n: int) -> int:
        
        a, b = 1, 1

        for _ in range(2, n + 1):
            # count ways to reach the current step
            current = a + b
            b = a

            a = current

        return a



