class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return false # can't add letters
        '''
        we keep a dictionary of sChar:tChar. Whenever we get to an index where we have to change it,
        we record that s->t change as sChar:tChar. If sChar does not have to change, we record sChar:sChar

        If we come across another instance of sChar that has to be changed to a DIFFERENT tChar(2), but sChar
        already is mapped to tChar(1), then we return false

        If the loop exits with no break we return true
        '''
        mapping = {}
        alreadyUsed = set()

        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            if sChar in mapping and mapping[sChar] != tChar:
                return False
            elif sChar not in mapping:
                if tChar in alreadyUsed:
                    return False
                mapping[sChar] = tChar
                alreadyUsed.add(tChar)
        return True