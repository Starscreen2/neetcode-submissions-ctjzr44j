class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = {}
        tt = {}

        for i in s:
            if i in ss:
                ss[i] += 1
            else:
                ss[i] = 1
        for j in t:
            if j in tt:
                tt[j] += 1
            else:
                tt[j] = 1

        return tt == ss


