'''
brute force solution: try starting at EVERY station and return the FIRST that loops back onto itself
O(n^2) time complexity though...
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute force:
        def solve(start_index)->bool:
            fuel = 0
            for j in range(start_index,start_index+len(gas)):
                idx = j%len(gas)
                fuel += gas[idx]
                fuel-= cost[idx]
                if fuel < 0:
                    return False
            return True


        for i in range(len(gas)):
            if solve(i):
                return i
        return -1