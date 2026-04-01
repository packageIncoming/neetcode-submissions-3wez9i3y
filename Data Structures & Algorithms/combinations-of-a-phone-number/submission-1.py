class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        combinations = [""]

        # iterative solution
        for digit in digits:
            curState = combinations.copy()
            newState = []
            for combo in curState:
                for i in range(len(mapping[digit])):
                    newState.append(combo + mapping[digit][i])
            combinations = newState
        return combinations