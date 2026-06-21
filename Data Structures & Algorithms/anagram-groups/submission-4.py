class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            tup = [0]*26
            for c in word:
                tup[ord(c)-ord('a')]+=1
            tup = tuple(tup)
            if tup not in groups:
                groups[tup] = [word]
            else:
                groups[tup].append(word)


        return list(groups.values())