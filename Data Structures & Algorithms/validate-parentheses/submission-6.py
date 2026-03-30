class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        temp = []


        for p in s:
            if p in d:
                if not temp or temp[-1] != d[p]: 
                    return False
                temp.pop()
            else:
                temp.append(p)

        return len(temp) == 0