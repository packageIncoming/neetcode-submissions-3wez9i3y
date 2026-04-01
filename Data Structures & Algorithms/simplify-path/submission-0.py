class Solution:
    def simplifyPath(self, path: str) -> str:
        # two pointers?

        l =0
        pieces = []
        while l < len(path):
            # consume /'s
            while l < len(path) and path[l] == '/':
                l+=1
            # now l should point to something that doesn't equal '/' so it's directory or . or ..
            if l >= len(path):
                break
            part = ""
            while l < len(path) and path[l] != "/":
                part+= path[l]
                l+=1
            # now this should represent a section
            # if it's a . then nothing happens
            # if it's a .. that means we went up one so we remove the last added piece
            # otherwise we add it to the list
            if part == '.':
                continue
            elif part == '..' :
                if len(pieces) > 0:
                    pieces.pop()
            else:
                pieces.append(part)
            
            # then move l onto the next
            l+=1
       # print(pieces)

        return "/" + "/".join(pieces)