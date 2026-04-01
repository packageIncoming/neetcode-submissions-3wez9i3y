class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursePrereqs = [0 for i in range(numCourses)] # i = course, arr[i] = prereqs count for course i 
        coursesRelyingOnCourse= [set() for i in range(numCourses)] # i = course, arr[i] = classes with course i as a prereq
        # 1. populate lists
        for p in prerequisites:
            course = p[0]
            prereq = p[1]
            coursePrereqs[course] +=1
            coursesRelyingOnCourse[prereq].add(course)
        
        finishedSet = set()
        q = collections.deque()

        for course in range(numCourses):
            prereqs = coursePrereqs[course] 
            if prereqs == 0:
                q.append(course)
        while q:
            course = q.popleft()
            if coursePrereqs[course] == 0 and course not in finishedSet:
                finishedSet.add(course)
                for nextCourse in coursesRelyingOnCourse[course]:
                    coursePrereqs[nextCourse]-=1
                    if coursePrereqs[nextCourse] == 0 and nextCourse not in finishedSet:
                        q.append(nextCourse)
        
        return len(finishedSet) == numCourses