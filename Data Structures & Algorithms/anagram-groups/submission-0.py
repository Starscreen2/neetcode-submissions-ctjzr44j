class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()
        
        
        # list_1 = {}
        
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        
        #     if sorted_word not in list_1:
        #         list_1[sorted_word] = []

        #     list_1[sorted_word].append(word)

        # return list(list_1.values())











#Do not tell me the answer, this is a learning opportunity for me and for me to learn only, so please prioritize me doing all fo the coding. And please provide me examples to do something if necessary(make sure the example give me the answer to the problem I am focusing on). Act as a tutor