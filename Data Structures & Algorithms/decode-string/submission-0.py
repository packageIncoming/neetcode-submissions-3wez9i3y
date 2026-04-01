class Solution:
    def decodeString(self, s: str) -> str:


        def buildString(i,substr):
            if i >= len(substr):
                return ""
            if substr[i].isalpha():
                return substr[i] + buildString(i+1,substr)
            if substr[i] == '[' or substr[i] == ']':
                return buildString(i+1,substr)
            if substr[i].isdigit():
                num = ""
                while substr[i].isdigit():
                    num+=substr[i]
                    i+=1
                # now i should be pointing to a [
                i+=1
                # construct the inner substring
                inner = ""
                leftCount = 1
                while i < len(substr) and leftCount >0:
                    if substr[i] == '[': leftCount+=1
                    elif substr[i] == ']': leftCount-=1
                    inner+=substr[i]
                    i+=1
                # now s[i] should point to where the next part starts
                return int(num) * buildString(0,inner) + buildString(i,substr)
            
        return buildString(0,s)