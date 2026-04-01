class MinStack:
    '''Implementation Details:
        Each element in self.elems is a tuple with (element,minimum), and minimum is the
        minimum value of the stack up to that point (including element)
    '''
    def __init__(self):
        self.elems = []
        self.size = 0

    def push(self, val: int) -> None:
        if self.size > 0:
            top_element = self.elems[-1]
            top_min = top_element[1]
            minimum = min(val,top_min)
            self.elems.append((val,minimum))
        else:
            self.elems.append((val,val))
        self.size+=1


    def pop(self) -> None:
        self.elems.pop()
        self.size-=1

    def top(self) -> int:
        return self.elems[-1][0]

    def getMin(self) -> int:
        return self.elems[-1][1]
