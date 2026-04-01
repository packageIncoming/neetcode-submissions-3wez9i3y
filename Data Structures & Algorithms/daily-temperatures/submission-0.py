class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        dailyTempsStreaks = []
        #Naive O(n^2) solution
        for i in range(len(temperatures)):
            higherTempFound = False
            for j in range (i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    dailyTempsStreaks.append(j-i)
                    higherTempFound = True
                    break
            if not higherTempFound:
                dailyTempsStreaks.append(0)

        return dailyTempsStreaks
