class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        queue1 = {}
        queue2 = {}

        for character in s:
            if character in queue1:
                queue1[character] += 1
            else:
                queue1[character] = 1

        for character in t:
            if character in queue2:
                queue2[character] += 1
            else:
                queue2[character] = 1

        return queue1 == queue2
