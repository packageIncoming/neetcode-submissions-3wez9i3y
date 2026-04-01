class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        maxHeap = []
        if a>0:
            maxHeap.append([-a,'a'])
        if b > 0:
            maxHeap.append([-b,'b'])
        if c > 0:
            maxHeap.append([-c,'c'])
        
        heapq.heapify(maxHeap)

        res=""
        while maxHeap:
            print(res,maxHeap)
            # find most 
            firstCount,firstChar = heapq.heappop(maxHeap)
            # get second most
            secondCount, secondChar = None,None
            if maxHeap:
                secondCount, secondChar = heapq.heappop(maxHeap)
            
            # 2 options: res is about to do 3 letters in a row or it is not
            # if it is not then add as regular
            # if it is then add the second count instead
            if len(res) >1 and res[-1] == res[-2] and res[-1] == firstChar:
                # about to do triplet, avoid this
                if secondChar is None:
                    # no second character exists so there's no way to fix this
                    break
                else:
                    secondCount+=1
                    res+=secondChar
                    heapq.heappush(maxHeap,[firstCount,firstChar])
                    if secondCount < 0:
                        heapq.heappush(maxHeap,[secondCount,secondChar])
            else:
                # not worried about triplet
                firstCount+=1
                res+=firstChar
                if firstCount < 0:
                    heapq.heappush(maxHeap,[firstCount,firstChar])
                if secondCount and secondChar:
                    heapq.heappush(maxHeap,[secondCount,secondChar])

        return res
                