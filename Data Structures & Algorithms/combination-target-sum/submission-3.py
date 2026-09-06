class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort the numbers so we can stop once its too large
        nums.sort()
        answer = []
        current = []
        def backtrack(start, remaining):
            # save a copy because current changes later
            if not remaining:
                answer.append(current.copy())
                return 
            #try every number that can still possibly fit
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break
                #choose this number and allow it to be used again
                current.append(nums[i])
                backtrack(i, remaining - nums[i])
                #undo choice before trying next numeber
                current.pop()
        #start from index 0 with the full target
        backtrack(0, target)
        return answer