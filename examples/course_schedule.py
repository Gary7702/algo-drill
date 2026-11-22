"""Course Schedule: decide whether every course can be finished."""

from collections import deque


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """Approach: Kahn topological sort (BFS) over the prerequisite graph.

    Time O(V + E), space O(V + E).
    """
    graph: list[list[int]] = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
    completed = 0
    while queue:
        course = queue.popleft()
        completed += 1
        for nxt in graph[course]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return completed == num_courses
