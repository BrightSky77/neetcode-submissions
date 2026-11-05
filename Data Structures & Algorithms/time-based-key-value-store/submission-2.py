class TimeMap:

    def __init__(self):
        self.key_value = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.key_value[key]:
            return ""
        l,r = 0,len(self.key_value[key])-1
        ans_idx = -1
        while l<=r:
            mid = (l+r) // 2
            if self.key_value[key][mid][1] <= timestamp:
                ans_idx = mid
                l = mid + 1
            else:
                r = mid -1
        if ans_idx == -1:
            return ""
        return self.key_value[key][ans_idx][0]

        
