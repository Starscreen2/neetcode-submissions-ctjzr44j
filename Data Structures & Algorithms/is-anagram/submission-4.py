class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset1 = {}
        hashset2 = {}


        for char in s:
            if char in hashset1:
                hashset1[char] += 1
            else:
                hashset1[char] = 1

        for char in t:
            if char in hashset2:
                hashset2[char] += 1
            else:
                hashset2[char] = 1

        return hashset1 == hashset2
