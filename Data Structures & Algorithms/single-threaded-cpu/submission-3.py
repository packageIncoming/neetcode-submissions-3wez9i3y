'''
Obviously a heap problem in my opinion
Heap objects: [enqueueTime,processingTime,taskIndex]
CPU should have an internal clock to represent the current time 
'''


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        # create the stack of tasks (from highest to lowest enq time)
        taskStack = []
        for i in range(len(tasks)):
            task = tasks[i]
            taskStack.append([task[0],task[1],i]) #[enqTime,procTime,taskIdx]
        taskStack.sort(key=lambda x:x[0],reverse=True)
        print(taskStack)
        minHeap = []
        curTime = taskStack[-1][0]
        res=[]
        while taskStack:
            curTime = max(curTime,taskStack[-1][0]) # handles 'idling' (last task done didn't take long enough for the next to be ready)
            while taskStack and taskStack[-1][0] <= curTime:
                enqTime,procTime,taskIdx = taskStack.pop()
                heapq.heappush(minHeap,[procTime,taskIdx])
            print(minHeap)
            # now we have a list of all tasks that can be done
            topTime,topIdx = heapq.heappop(minHeap)
            curTime+=topTime
            res.append(topIdx)
            
        while minHeap:
            time,idx = heapq.heappop(minHeap)
            curTime+= time
            res.append(idx)
        return res
        