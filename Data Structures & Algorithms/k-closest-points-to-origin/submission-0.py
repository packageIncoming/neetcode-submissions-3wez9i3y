'''
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on 
an X-Y axis plane.
    - Primary input, points = 2D array
You are also given an integer k.

Return the k closest points to the origin (0, 0).
    -Obviously a heap question, min or max heap??
        *Question asks for the closest points, so we want d to be minimal, so minheap

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
    - Use a helper function to determine distance?

Algorithm:
    - Calculate distance for each point, save in tuple pairs into new array pointsWithDistanceToOrigin[]
    - heapify pointsWithDistanceToOrigin
    - return k points from pointsWithDistanceToOrigin


Example Walkthrough
Input: points = [[0,2],[2,0],[2,2]], k = 2
    1. pointsWithDistanceToOrigin = [([0,2],2),([2,0],2),([2,2],2.83)]
    2. pop from pointsWithDistanceToOrigin until res array has k elements: [[0,2],[2,0]]
    3. return res = [[0,2],[2,0]]
Output: [[0,2],[2,0]]
'''

class Solution:
    def distanceToOrigin(self,point):
        return math.sqrt(point[0]**2 + point[1]**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointsWithDistanceToOrigin = [(self.distanceToOrigin(point),point) for point in points]
        heapq.heapify(pointsWithDistanceToOrigin)
        res = []
        while len(res) < k:
            res.append(heapq.heappop(pointsWithDistanceToOrigin)[1])
        return res
        





