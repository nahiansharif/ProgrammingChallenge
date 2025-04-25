# https://leetcode.com/problems/course-schedule-ii/ 

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


from typing import List

class Solution:
    def dfs(self, i: int, adj: List[List[int]], hash: set, visited: List[bool], stack: List[int]) -> bool:
        hash.add(i)
        visited[i] = True

        for neighbor in adj[i]:
            if not visited[neighbor]:
                if not self.dfs(neighbor, adj, hash, visited, stack):
                    return False
            elif neighbor in hash:
                return False

        hash.remove(i)
        stack.append(i)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj[src].append(dest)

        visited = [False] * numCourses
        stack = []

        for i in range(numCourses):
            if not visited[i]:
                hash = set()
                if not self.dfs(i, adj, hash, visited, stack):
                    return []

        return stack[::-1] 
    
    
from collections import defaultdict, deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []
    
    
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        sorted_order = []
        # if n is smaller than or equal to zero we will return the empty array
        if n <= 0:
            return sorted_order

        # Store the count of incoming prerequisites in a hashmap
        in_degree = {i: 0 for i in range(n)}
        # a. Initialize the graph
        graph = {i: [] for i in range(n)}  # adjacency list graph

        # b. Build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[1], prerequisite[0]
            graph[parent].append(child)  # add the child to its parent's list
            in_degree[child] += 1  # increment child's in_degree

        # c. Find all sources i.e., all nodes with 0 in-degrees
        sources = deque()
        # traverse in in_degree using key
        for key in in_degree:
            # if in_degree[key] is 0 append the key in the deque sources
            if in_degree[key] == 0:
                sources.append(key)

        # d. For each source, add it to the sorted_order and subtract one from
        # all of its children's in-degrees. If a child's in-degree becomes zero,
        # add it to the sources queue
        while sources:
            # pop an element from the start of the sources and store
            # the element in vertex
            vertex = sources.popleft()
            # append the vertex at the end of the sorted_order
            sorted_order.append(vertex)
            # traverse in graph[vertex] using child
            # get the node's children to decrement
            # their in-degrees
            for child in graph[vertex]:
                in_degree[child] -= 1
                # if in_degree[child] is 0 append the child in the deque sources
                if in_degree[child] == 0:
                    sources.append(child)

        # topological sort is not possible as the graph has a cycle
        if len(sorted_order) != n:
            return []

        return sorted_order
    
    