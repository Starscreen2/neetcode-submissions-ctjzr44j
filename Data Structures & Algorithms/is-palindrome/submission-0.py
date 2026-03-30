class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for char in s:
            if char.isalnum():
                r += char.lower()
        return r[::-1] == r


