class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        used = [False] * len(strs)
        res = []

        def count_letters(word: str) -> dict:
            temp = {}
            for ch in word:
                if ch in temp:
                    temp[ch] += 1
                else:
                    temp[ch] = 1
            return temp

        for i in range(len(strs)):
            if used[i]:
                continue

            base_count = count_letters(strs[i])
            group = [strs[i]]
            used[i] = True

            for j in range(i + 1, len(strs)):
                if used[j]:
                    continue
                if count_letters(strs[j]) == base_count:
                    group.append(strs[j])
                    used[j] = True

            res.append(group)

        return res
            