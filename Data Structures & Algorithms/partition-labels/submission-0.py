class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alpha_lst_index = defaultdict(list)
        n = len(s)

        for r in range(n):
            if s[r] in alpha_lst_index:
                continue
            j = r
            alpha_lst_index[s[r]].append(r)
            while j < n:
                if s[r] == s[j]:
                    max_index = j
                j += 1
            alpha_lst_index[s[r]].append(max_index)
        
        # [[1,4],[2,5],[3,7]]
        alpha_lst_index = list(alpha_lst_index.values())

        res = [alpha_lst_index[0]]

        for idx in range(1,len(alpha_lst_index)):
            prev_start, prev_end = res[-1]
            start,end = alpha_lst_index[idx]

            if prev_end > start:
                if end > prev_end:
                    res[-1][1] = end
            else:
                res.append(alpha_lst_index[idx])
        
        ans = []
        for start,end in res:
            ans.append(end-start+1)
        return ans


        
        
        

        

            

        

                
            
        
        