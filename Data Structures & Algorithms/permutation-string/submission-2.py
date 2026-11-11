class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = count1.get(c,0) + 1
        
        n1 = len(s1)
        n2= len(s2)
        for i in range(n2):
            curr = 0
            count2 = {}
            for j in range(i,i+n1):
                if j >= n2:
                    break
                count2[s2[j]] = count2.get(s2[j],0) + 1
                if s2[j] not in count1:
                    break

                if (count2[s2[j]] == count1[s2[j]]):
                    curr += 1

                if curr == len(count1):
                    return True
        
        return False

                
                




        





