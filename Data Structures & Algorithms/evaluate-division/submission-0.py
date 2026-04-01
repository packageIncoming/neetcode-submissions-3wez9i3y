'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
-   2 inputs, array of equations [var1,var2] and array of the results var1/var2=value
-   3rd input represents unsolved queries [var1,var2]
-   GOAL: SOLVE THE UNSOLVED QUERIES OR PUT -1 IF UNSOLVABLE
-   Variables that are not in the list of equations are undefined so an answer cannot be determined 
    for them

-Idea:
    Represent variable divisions as a directed graph
    a->b with connection 'weight' x where a = x*b
    Create the directed graph as a hashmap of hashmaps
    variable: connection list
        connection list = connectedVariable: x
    
    When given two variables v1 and v2, start at (v1,1) and travel v1's connections until you get to
    v2. At each each you multiply by x which is the division value

    If you can't reach v2 then return -1

'''



class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # create directed graph:
        conns = {}
        for i in range(len(equations)):
            v1,v2 = equations[i]
            div = values[i]
            #v1 = v2*div
            conns[v1] = conns.get(v1,{})
            conns[v1][v2] = div
            # v2 = v1/div
            conns[v2] = conns.get(v2,{})
            conns[v2][v1] = 1/div
        def travel(cur,target,value,seen):
            if cur in seen or cur not in conns:
                return None # invalid going back
            if cur == target:
                return value # base case

            
            seen.add(cur)
            connections = conns[cur]
            for connection in connections:
                pathRes = travel(connection,target,value*connections[connection],seen)
                if pathRes is not None:
                    return pathRes
            return None
            
        
        res = []
        for v1,v2 in queries:
            attempt = travel(v1,v2,1,set())
            if attempt is not None:
                res.append(attempt)
            else:
                res.append(-1)
        
        return res
            

