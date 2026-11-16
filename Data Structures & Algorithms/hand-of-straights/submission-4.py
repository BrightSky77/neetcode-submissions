class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if (n % groupSize) != 0:
            return False
        
        hand.sort()
        count = Counter(hand)

       
        for x in hand:
            hand_cnt = count[x]
            if count[x] == 0:
                continue
            
            for group_split in range(x,x+groupSize):
                if count[group_split] < hand_cnt:
                    return False
                count[group_split] -= hand_cnt
        return True


        