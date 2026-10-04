class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}

        for char in s:
            if char in a:
                a[char] += 1
            else:
                a[char] = 1

        for char in t:
            if char in b:
                b[char] += 1
            else:
                b[char] = 1
        
        return a == b