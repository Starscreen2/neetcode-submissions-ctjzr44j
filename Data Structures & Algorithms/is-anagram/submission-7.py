class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmaps = {}
        hashmapt = {}

        for i in s:
            if i in hashmaps:
                hashmaps[i] += 1
            else:
                hashmaps[i] = 1

        for i in t:
            if i in hashmapt:
                hashmapt[i] += 1
            else:
                hashmapt[i] = 1

        return hashmaps == hashmapt
        




