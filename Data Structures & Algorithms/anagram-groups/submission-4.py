class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        anagram_dict = defaultdict(list)
        
        for i in range(len(strs)):
            sorted_strs_set = tuple((sorted(strs[i])))
            anagram_dict[sorted_strs_set].append(strs[i])
        
        return list(anagram_dict.values())
            




        
        
        
        
        
        
        # res = defaultdict(list)
        # for st in strs:
        #     count = [0] * 26
        #     for c in st:
        #         count[ord(c)-ord('a')] += 1
        #     res[tuple(count)].append(st)
        # return list(res.values())


            

        