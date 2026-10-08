class Solution:
    def isValid(self, s: str) -> bool:
        dictt = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        stack = []

        for p in s:
            if p in dictt:
                if stack and stack[-1] == dictt[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
            
        if not stack:
            return True
        return False