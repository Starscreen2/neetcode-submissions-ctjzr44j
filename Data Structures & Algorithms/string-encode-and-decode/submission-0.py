class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):  # Use 's' instead of 'str'
            j = i
            while s[j] != "#":  # Use 's' instead of 'str'
                j += 1
            length = int(s[i:j])  # Use 's' instead of 'str'
            res.append(s[j + 1 : j + 1 + length])  # Use 's' instead of 'str'
            i = j + 1 + length
        return res
