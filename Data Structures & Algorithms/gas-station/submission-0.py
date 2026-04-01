class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute force solution, starting from every single station and trying to get to that same station

        for start in range(len(gas)):
            curGas = gas[start] - cost[start]
            i= (start+1)%len(gas)
            while curGas >= 0:
                if i == start: return start
                curGas += gas[i] - cost[i]
                i = (i+1)%len(gas)
        return -1
