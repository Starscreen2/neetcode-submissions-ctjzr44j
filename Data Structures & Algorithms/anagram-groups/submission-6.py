class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        everything = {}

        for i in strs:
            key = "".join(sorted(i))
            if key not in everything:
                everything[key] = []

            everything[key].append(i)

        return list(everything.values())

            
        