'''
-   Wheels can wrap around 0->9 or 9-> 0
-   1 move = moving ONE slot ONCE
-   Starts at 0000
-   Wheels move independently
-   If the lock displays a deadend code then it kills that branch
-   GOAL: Return minmum # of turns to open lock OR -1 if impossible
-   Since wheels move independently there's 4 subproblems 
-   Since each wheel starts at 0 it can ONLY go (0 1 2 3 4 5 6 7 8 9 ) OR (0 9 8 7 6 5 4 3 2 1)

-   Backtracking? Kind of like N queens it feels

'''


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)

        def getNextStates(state):
            nxt = []
            for wheelIdx in range(4):
                newWheelValue = (int(state[wheelIdx])+1)%10
                newWheelValueBackwards = (int(state[wheelIdx])-1 + 10) % 10
                newStateUp = state[:wheelIdx] + str(newWheelValue) + state[wheelIdx+1:]
                newStateDown = state[:wheelIdx] + str(newWheelValueBackwards) + state[wheelIdx+1:]
                nxt.append(newStateUp)
                nxt.append(newStateDown)
            return nxt
        q = deque()
        q.append(['0000',0])
        while q:
            cur = q.popleft()
            state = cur[0]
            turns = cur[1]
            if state == target:
                return turns
            if state in seen: continue # don't look
            seen.add(state)
            for newState in getNextStates(state):
                q.append((newState,turns+1))
        return -1