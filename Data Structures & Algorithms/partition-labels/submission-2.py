class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i,c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size = end = 0
        for i,c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res

        # alpha_lst_index = {}
        # n = len(s)

        # # for r in range(n):
        # #     if s[r] in alpha_lst_index:
        # #         continue
        # #     j = r
        # #     alpha_lst_index[s[r]].append(r)
        # #     while j < n:
        # #         if s[r] == s[j]:
        # #             max_index = j
        # #         j += 1
        # #     alpha_lst_index[s[r]].append(max_index)

        # for r in range(n):
        #     if s[r] not in alpha_lst_index:
        #         alpha_lst_index[s[r]] = [r,r]
        #     else:
        #         alpha_lst_index[s[r]][1] = r
        
        # # [[1,4],[2,5],[3,7]]
        # alpha_lst_index = list(alpha_lst_index.values())

        # res = [alpha_lst_index[0]]

        # for idx in range(1,len(alpha_lst_index)):
        #     prev_start, prev_end = res[-1]
        #     start,end = alpha_lst_index[idx]

        #     if prev_end > start:
        #         if end > prev_end:
        #             res[-1][1] = end
        #     else:
        #         res.append(alpha_lst_index[idx])
        
        # ans = []
        # for start,end in res:
        #     ans.append(end-start+1)
        # return ans


        
        
        

        

            

        

                
            
        
        