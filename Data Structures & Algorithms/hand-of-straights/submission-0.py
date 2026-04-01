class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False # can't evenly divide into groups of groupSize
        hand.sort()
        hmap = defaultdict(int)
        for num in hand:
            hmap[num]+=1
        
        count = 0
        for start_num in hand:
            while hmap[start_num] >0:
                hmap[start_num]-=1
                size = 1
                nxt = start_num+1
                while size < groupSize:
                    if nxt not in hmap or hmap[nxt] <= 0:
                        return False
                    else:
                        hmap[nxt] -=1
                        size+=1
                        nxt+=1
                count+=1
                if count == (len(hand)//groupSize): return True