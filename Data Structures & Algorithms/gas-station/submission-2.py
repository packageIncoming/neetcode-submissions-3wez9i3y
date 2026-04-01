class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # optimized o(n) solution, perhaps a modification of kadane's would work?
        STOPS = len(gas)
        start = 0
        curGas = 0
        traveled = 0
        for i in range(STOPS*2):
            idx = i%len(gas)
            
            curGas += gas[idx] - cost[idx]
            if curGas < 0:
                # can't make it to the next station
                start = (idx+1)%len(gas)
                curGas=0
                traveled=0
            else:
                traveled+=1
            if traveled == STOPS:
                return start
        return -1

        # brute force solution, starting from every single station and trying to get to that same station
        # o(n^2) time complexity, o(1) space complexity
        for start in range(len(gas)):
            curGas = gas[start] - cost[start]
            i= (start+1)%len(gas)
            while curGas >= 0:
                if i == start: return start
                curGas += gas[i] - cost[i]
                i = (i+1)%len(gas)
        return -1
