class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dictt = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for i in s:
            if i in dictt:
                if stack and stack[-1] == dictt[i]:
                    stack.pop()
                else: return False
            else:
                stack.append(i)
            
        if not stack:
            return True
        return False