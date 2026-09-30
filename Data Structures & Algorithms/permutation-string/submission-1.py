class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        need = Counter(s1)
        window = Counter(s2[:m])

        for i in range(len(s2) - m + 1):
            if window == need:
                return True
            
            if i + m < len(s2):
                left = s2[i]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]
                window[s2[i + m]] += 1

        return False