class CountSquares:

    def __init__(self):
        self.pointsCount = {}
        self.points = []
    def add(self, point: List[int]) -> None:
        coords = tuple(point)
        if coords in self.pointsCount:
            self.pointsCount[coords]+=1
        else:
            self.pointsCount[coords]=1
        self.points.append(point)
            

    def count(self, point: List[int]) -> int:
        qx,qy = point[0],point[1]
        res=0
        # check for diagonal
        for x,y in self.points:
            if abs(qx-x) == abs(qy-y) and abs(qx-x) !=0:
                # valid diagonal
                p1 = (qx,y)
                p2 = (x,qy)
                if p1 in self.pointsCount and p2 in self.pointsCount:
                    res += self.pointsCount[p1] * self.pointsCount[p2]
        return res