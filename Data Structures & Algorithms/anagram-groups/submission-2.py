class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bins = defaultdict(list)
        for s in strs:
            c = [0]*26
            for char in s:
                c[ord(char) - ord('a')] +=1
            bins[tuple(c)].append(s)
        return list(bins.values())