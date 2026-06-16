
'''
i think this involves a heap in some manner
the issue is in bringing the time complexities of both
addScore and top(k) down 

because you can easily do the following:
- Instantiate an empty maxheap
addScore:
    O(n) check if existing, 
        yes-> update score then heapify() O(nlogn)
        no-> push new tuple (id,score) O(logn)
    Worst case becomes O(NLOGN) for addScore
top(k):
    O(nlogk) if popping from top k times & then adding them back in
    Worst case scenario would be O(nlogn)

But that's kind of the worst of the worst since you could do:
addScore:
    append & then sort()
    O(nlogn)
topK:
    just grab array[:k]
    O(1)
reset():
    del[], O(n) at worst

What data structure or datastructures can provide O(1) lookup
and as close to O(n) or maybe even O(1) SORTED insertions?

Hashmap for storing the values
Minheap for getting top k score


'''

class Leaderboard:

    def __init__(self):
        self.scores={}

        

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = self.scores.get(playerId,0)+score

    def top(self, K: int) -> int:
        heap = []
        for pid in self.scores:
            score = self.scores[pid]
            if len(heap)<K:
                heapq.heappush(heap,score)
            else:
                if score > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,score)
        print(heap)
        return sum(heap)
        

    def reset(self, playerId: int) -> None:
        self.scores[playerId]=0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
