class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split('/')
        res=[]

        for d in p:
            if d == '.':
                continue
            elif d == '..':
                if res:
                    res.pop()
            elif d == '':
                continue
            else:
                res.append(d)
        

        return '/' + '/'.join(res) 