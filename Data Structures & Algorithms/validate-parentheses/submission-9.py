class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        stack = []

        for character in s:
            if character in dictionary:
                if stack and stack[-1] == dictionary[character]:
                    stack.pop()
                else: return False
            else:
                stack.append(character)
            
        if not stack:
            return True
        
        return False
