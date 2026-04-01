class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution idea: Iterate over all of the strings in strs and sort each of them
        # Have a hashmap that has the keys as the sorted string and the value as a list
        # of strings (non-sorted, original). Lookup the sorted string, if it exists then add it
        # to that list, if not initialize it. At the end, combine all .values() into a single list 
        # and return that list
        visited = {}
        for s in strs:
            ss = "".join(sorted(s))
            if visited.get(ss,None) is None:
                visited[ss] = [s]
            else:
                visited[ss].append(s)
        return list(visited.values())