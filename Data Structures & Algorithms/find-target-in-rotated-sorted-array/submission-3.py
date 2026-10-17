class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        pivot = l
        l,r = 0, len(nums)-1

        def binarysearch(l,r,target):
            while l <= r:
                m = (l+r)//2
                if nums[m] > target:
                    r = m - 1
                elif nums[m]  < target:
                    l = m + 1
                else:
                    return m
            return -1

        
        result = binarysearch(0,pivot-1,target)
        if result != -1:
            return result
        return binarysearch(pivot,r,target)


        