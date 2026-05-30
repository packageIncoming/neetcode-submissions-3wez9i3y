'''
There's two problems at hand
Storing
Retrieving

retrive returns the ids of the logs within the timestamp range
    retrieve also has granularity

I think the obvious solution in terms of timestamps
is to parse and then turn it into seconds
Year is always between 2000 and 2017

However there's also a Trie solution here I think
Year-Month-Day-Hour-Minute-Second

But is there a simpler solution that works
I think the Trie IS the simple thing because you just have to parse
and then append

Actually wouldn't regex work??
That's what the example seems to point towards:

logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour");
// return [2,1], because you need to return all logs between Jan. 1, 2016
// 01:XX:XX and Jan. 1, 2017 23:XX:XX.
// Log 3 is not returned because Jan. 1, 2016 00:00:00 comes before the
// start of the range.

What if two logs have the same timestamp though

I'll go for the brute force solution first which is a hash table and range check?

'''

lookup = {
    'Year':4,
    'Month':7,
    'Day':10,
    'Hour':13,
    'Minute':16,
    'Second':18
}


class LogSystem:

    def __init__(self):
        self.table = {}


    def put(self, id: int, timestamp: str) -> None:
        self.table[id] = timestamp

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        res=[]
        idx = lookup[granularity]+1
        s = start[:idx]
        e = end[:idx]
        for id, timestamp in self.table.items():
            if s<= timestamp[:idx] <= e:
                res.append(id)


        return res



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
