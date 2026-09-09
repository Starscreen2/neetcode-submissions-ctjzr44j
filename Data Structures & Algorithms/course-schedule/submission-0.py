class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create a graph where each prerequisites points to the courses that need int
        # store the state of every courses
        #- 0 means we have not visited
        #- 1 it is currently in the DFS path
        #- 2 means we already checked it and found no cycle
        #dfs from every course if dfs reachees a course with state 1, we found cycle
        #if 2, we know its already safe
        #once we checked all neighbors, we mark the current cources as safe, return false false if a cycle is found else true

        # Create one empty list for every course
        graph = [[] for _ in range(numCourses)]
        # add a directed edge from the pre req to the course
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        state = [0] * numCourses
        #store the visit state for every course

        #check weather starting from this course leads to a cycle
        def has_cycle(course):
            if state[course] == 1:
                return True
            if state[course] == 2:
                return False
            
            #mark this course as being explored in the path
            state[course] = 1
            for next_course in graph[course]:
                if has_cycle(next_course):
                    return True
            #all paths are safe stating from this course
            state[course] = 2
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True
