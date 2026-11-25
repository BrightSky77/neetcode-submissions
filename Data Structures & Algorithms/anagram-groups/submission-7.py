class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for alphabet in s:
                count[ord('a')-ord(alphabet)] += 1
            res[tuple(count)].append(s)
        return list(res.values())


        # if not strs:
        #     return [[""]]
        # anagram_dict = defaultdict(list)
        
        # for i in range(len(strs)):
        #     sorted_strs_set = "".join(sorted(strs[i]))
        #     anagram_dict[sorted_strs_set].append(strs[i])
        
        # return list(anagram_dict.values())


            

        