class MyCircularQueue:

    class Node:
        def __init__(self,val:int):
            self.val=val
            self.next=None
            self.prev=None
        

    def __init__(self, k: int):
        self.limit=k
        self.size=0
        self.head=None
        self.tail=None

    def enQueue(self, value: int) -> bool:
        if self.size==self.limit:
            return False
        #special case where size == 0 so new node is both head AND tail
        self.size+=1
        node = self.Node(value)

        if self.size==1:
            self.head=node
            self.tail=node
            return True

        self.tail.next=node
        node.prev=self.tail

        self.tail=node
        return True


    def deQueue(self) -> bool:
        if self.size <=0:
            return False
        #special case where size == 1 so popping what is the head and tail
        if self.size==1:
            self.tail=None
            self.head=None
            self.size-=1
            return True
        # otherwise for size >=2 we have to update the head
        newHead = self.head.next
        del self.head
        self.head=newHead
        self.size-=1
        return True


    def Front(self) -> int:

        return self.head.val if self.head else -1

    def Rear(self) -> int:
        return self.tail.val if self.tail else -1
        

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()