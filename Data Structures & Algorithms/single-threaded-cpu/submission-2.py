'''
Obviously a heap problem in my opinion
Heap objects: [enqueueTime,processingTime,taskIndex]
CPU should have an internal clock to represent the current time 
'''


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #  create heap and start time
        minHeap = []
        curTime = float('inf')
        for i in range(len(tasks)):
            task = tasks[i]
            minHeap.append([task[0],task[1],i])
            curTime = min(curTime,task[0])
        heapq.heapify(minHeap)

        #  begin processing heap to create order
        res=[]

        while minHeap:
            # get all available tasks
            innerHeap = []
            curTime = max(curTime,minHeap[0][0])
            while minHeap and minHeap[0][0] <= curTime:
                # add to inner heap as [processingTime,taskIndex,enqueueTime]
                task = heapq.heappop(minHeap)
                heapq.heappush(innerHeap,[task[1],task[2],task[0]])
            #print(innerHeap)
            procTime,taskIndex,enqTime = heapq.heappop(innerHeap)
            curTime = max(curTime,enqTime)
            curTime+=procTime
            res.append(taskIndex)
            while innerHeap:
                # add back onto the heap
                otherProcTime,otherIndex,otherEnqTime = heapq.heappop(innerHeap)
                heapq.heappush(minHeap, [otherEnqTime,otherProcTime,otherIndex])
        #print(res)
        return res