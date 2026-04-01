class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursePrereqs = [0 for i in range(numCourses)]
        reliantCourses = [[] for i in range(numCourses)]
        for course,prereq in prerequisites:
            coursePrereqs[course]+=1
            reliantCourses[prereq].append(course)
        
        q = collections.deque()
        for course in range(numCourses):
            if coursePrereqs[course] == 0:
                q.append(course)
        seen = set()
        orderedCourses = []
        while q:
            course = q.popleft()
            if coursePrereqs[course] == 0 and course not in seen:
                orderedCourses.append(course)
                seen.add(course)
                for nextCourse in reliantCourses[course]:
                    coursePrereqs[nextCourse]-=1
                    if coursePrereqs[nextCourse] == 0 and nextCourse not in seen:
                        q.append(nextCourse)
        if len(seen) == numCourses:
            return orderedCourses
        else:
            return []