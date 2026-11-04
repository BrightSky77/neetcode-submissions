class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_previous_dict = defaultdict(list)
        for cr,prev_cr in prerequisites:
            course_previous_dict[cr].append(prev_cr)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not course_previous_dict[course]:
                return True

            visited.add(course)
            for prev_course in course_previous_dict[course]:
                if not dfs(prev_course):
                    return False
            visited.remove(course)
            course_previous_dict[course] = []
            return True
        
        for r in range(numCourses):
            if not dfs(r):
                return False

        return True

        
        



        #time complexity O(V+)
        #Space complexity O()
        





        