'''
either kruskal's or DSU can solve this problem but I don't remember either 

! undirected so a->b means b->a
or perhaps topological sort

how would i do this as a human?
Input:
n = 5, edges = [[0,1],[1,2],[3,4]]
i keep track of who is connected to who. by default i say a node is connected to itself

0:0
1:1
2:2
3:3
4:4

i see that 0 is connected to 1. let's say whenever there is [from, to] that conns[to] = conns[from]
0:0
1:0
2:2
3:3
4:4

    
i see that 1 is connected to 2, i update 2's connection
0:0
1:0
2: conns[1] = 0
3:3
4:4
i see that 3 is connected to 4

0:0
1:0
2:0
3:3
4:3

When I've gone over all the edges I go through this mapping and count how many point to themselves
then I return this as the output
0:0
3:3
return 2

but what if it was [2,1] instead of [1,2]

then youd get:
0:0
1:2
2:2
3:3
4:3
return 3
which is WRONG

therefore you need to update the connection to the one that has more connected
so keep track of the 'degree' of each node

Output: 2

error on:
n=10
exp 4 got 3
edges=[[5,8],[3,5],[1,9],[4,5],[0,2],[7,8],[4,9]]

0:0
1:1
2:2
3:3
4:4
5:5
6:6
7:7
8:5
9:9
'''


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        conns = [i for i in range(n)]
        deg = [0 for i in range(n)]
        for fr,to in edges:
            frParent = fr
            while conns[frParent] != frParent:
                frParent = conns[frParent]
            print(fr,frParent)
            toParent = to
            while conns[toParent] != toParent:
                toParent = conns[toParent]
            frDeg = deg[conns[frParent]]
            toDeg = deg[conns[toParent]]
            if frDeg >= toDeg:
                deg[frParent]+=1
                conns[toParent] = frParent
            else:
                deg[toParent]+=1
                conns[frParent] = toParent
        res=0
        for i in range(n):
            print(i, conns[i])
            if conns[i] == i :
                res+=1
        return res
        