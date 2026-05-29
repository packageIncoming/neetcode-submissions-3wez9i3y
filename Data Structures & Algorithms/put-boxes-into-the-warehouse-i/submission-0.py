

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        heightsPrefix=[warehouse[0]]
        i=0
        count=0
        for room in warehouse:
            while i < len(boxes) and boxes[i] > room:
                i+=1 # Skip all the boxes permanently that cannot fit right now
                # A box that cannot fit now can never fit going down
                # since a box must be able to fit room r before getting to
                # room r+1
            if i == len(boxes):
                # we could not find a box that could fit this current room
                # meaning that we must end now 
                return count
            # if we reach here then we have a box that fits
            # but specifically we have the biggest box possible that fits here
            count+=1
            i+=1


        return count


