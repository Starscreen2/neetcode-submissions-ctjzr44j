class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        win_of_s = Counter()
        win_of_t = Counter(t)

        l, r = 0, 0
        have = 0
        need = len(win_of_t)
        best_start = 0
        best_len = float("inf")

        while r < len(s):
            char = s[r]
            win_of_s[char] += 1

            if char in win_of_t and win_of_s[char] == win_of_t[char]:
                have += 1

            while have == need:
                if r - l + 1 < best_len:
                    best_start = l
                    best_len = r - l + 1

                left_char = s[l]
                win_of_s[left_char] -= 1
                if left_char in win_of_t and win_of_s[left_char] < win_of_t[left_char]:
                    have -= 1
                l += 1

            r += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]