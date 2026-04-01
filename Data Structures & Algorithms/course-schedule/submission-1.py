class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0: return True # any order
        coursePrereqs = [set() for i in range(numCourses)] # i = course, arr[i] = prereqs for course i 
        coursesRelyingOnCourse= [set() for i in range(numCourses)] # i = course, arr[i] = classes with course i as a prereq
        # 1. populate lists
        for p in prerequisites:
            course = p[0]
            prereq = p[1]
            coursePrereqs[course].add(prereq)
            coursesRelyingOnCourse[prereq].add(course)
        
        finishedSet = set()
        def finishAndExplore(course):
            if len(coursePrereqs[course]) == 0:
                finishedSet.add(course)
                for nextCourse in coursesRelyingOnCourse[course]:
                    if course in coursePrereqs[nextCourse]:
                        coursePrereqs[nextCourse].remove(course)
                    finishAndExplore(nextCourse)

        # 2. find start courses (courses with no prereqs) and recursively explore them
        for course in range(numCourses):
            prereqs = coursePrereqs[course] 
            if len(prereqs) == 0:
                finishAndExplore(course)
        
        return len(finishedSet) == numCourses