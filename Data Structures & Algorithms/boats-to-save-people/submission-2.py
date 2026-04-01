'''
Notes/ideas:
    -Just by looking at the constraitns, there will be a LOT of people, up to 50,000
        Meaning anything more than O(n) probably won't work
        - So recursion probably wouldn't work
        - And using a queue prob wont work
    - No single person will be over the weight limit (second constraint)
    - There is an infinite number of boats

    Idea:
        - sort the input array, keep an ongoing sum with two pointers, whenever that sum
        - reaches the limit, increment boatCount and reset the sum to 0
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # efficient even for many 
        boatCount=0
        l,r = 0, len(people)-1
        while l <= r:
            if people[r] + people[l] <= limit:
                # both fit
                r-=1
                l+=1
                boatCount +=1
            else:
                # only the bigger one fits
                r-=1
                boatCount+=1


        
        return boatCount