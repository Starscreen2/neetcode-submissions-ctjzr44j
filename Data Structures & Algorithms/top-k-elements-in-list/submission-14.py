class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        #[] [] [] [] []
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        for n, c in count.items():
            freq[c].append(n)

        # [1] [2] [3]
        ls = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                ls.append(n)
                if len(ls) == k:
                    return ls