class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        res = defaultdict(list)
        for st in strs:
            word = ''.join(sorted(st))
            res[word].append(st)
        return list(res.values())

            

        