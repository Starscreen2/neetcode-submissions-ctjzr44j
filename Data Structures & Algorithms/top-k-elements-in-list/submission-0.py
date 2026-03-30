from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        count = Counter(nums)
        
        # Use a min-heap to keep track of the k most frequent elements
        return heapq.nlargest(k, count.keys(), key=count.get)