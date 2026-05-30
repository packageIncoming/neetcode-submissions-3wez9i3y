class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res=[]

        post=-1
        for i in range(len(heights)-1,-1,-1):
            if heights[i]>post:
                res.append(i)
            post = max(post,heights[i])


        res.reverse()
        return res