'''
Seems like the most capacity you'd need is if all the packages were the max weight 

ceil(len(weights) * max(weights) / days) is the upper limit (inclusive)

binary search a range from 1 to (upper limit)

run a shipAttempt(weights,capacity) using this capacity

if the number of days equals (days) then return that weight

if the number of days is greater than (days) then binary search the upper half (took too long)

if the number of days is less than (days) then binary search the lower half (update min weight then do so, could have lower weight)

return the found weight

O(n) for shipAttempt, ran at most log(n) times --> O(nlogn) time complexity

'''

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def shipAttempt(capacity):
            daysTaken = 0
            curTot= 0
            for weight in weights:
                if weight > capacity:
                    return float('inf') # invalid
                if curTot + weight <capacity:
                    curTot += weight
                elif curTot + weight == capacity:
                    curTot = 0
                    daysTaken+=1
                else:
                    curTot = weight
                    daysTaken+=1
            if curTot > 0:
                daysTaken+=1
            return daysTaken
        
        upperLimit =len(weights) * max(weights) 
        l,r = 1,upperLimit
        minCapacity = upperLimit
        print(upperLimit)
        while l<=r:
            m = (l+r)//2
            attempt = shipAttempt(m)
            print(m,attempt)
            if attempt > days:
                # took too long (too many days)
                l=m+1
            else:
                # succeeded but could've had a lower capacity
                minCapacity = min(minCapacity,m)
                r=m-1
        print(f"Min capcity: {minCapacity}")
        return minCapacity

