class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def toTuple(s):
            arr = [0]*26
            for c in s:
                arr[ord(c)-ord('a')]+=1
            return tuple(arr)
        h = defaultdict(list)
        for s in strs:
            h[toTuple(s)].append(s)
        return list(h.values())