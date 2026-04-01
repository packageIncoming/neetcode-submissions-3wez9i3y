class TimeMap:

    def __init__(self):
        self.values= defaultdict(list)
        # Dictionary where each value is a list of arrays [timestamp, value]
        # Since all calls to set() are in strictly increasing order we don't have to worry about updating previous
        #   timestamp values

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        keyValues = self.values[key]
        if len(keyValues) == 0: return ""
        #Binary Search algorithm
        l, r  = 0, len(keyValues)-1
        mostRecent = keyValues[0]
        while l <= r:
            mid = (l+r)//2
            currentTimestamp = keyValues[mid][0]
            if currentTimestamp == timestamp:
                return keyValues[mid][1]
            # update mostRecent
            if currentTimestamp > mostRecent[0] and currentTimestamp < timestamp:
                mostRecent = keyValues[mid]
            # update bounds and perform search again
            if currentTimestamp > timestamp:
                r=mid-1
            else:
                l=mid+1
        if mostRecent[0] < timestamp:
            return mostRecent[1]
        else:
            return ""