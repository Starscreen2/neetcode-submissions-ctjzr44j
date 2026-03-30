class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        temp = []

        for i in s:
            if i in dictionary:
                if not temp or temp[-1] != dictionary[i]:
                    return False
                else:
                    temp.pop()
            else:
                temp.append(i)
        return len(temp) == 0
                
            
                

