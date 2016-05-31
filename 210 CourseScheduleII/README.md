#[210 Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

## Notes:
1.	It's a directed graph problem, scince the vetices may have their parent pointing at them. So generate the graph first.
	The graph is mainly an array of vectors:
	
	    0: 1, 2 (Course 0 has two prerequisites: 1 and 2)
	    1: 3
	    2: 7
	    ...
	    ...
    
2.	Use depth-first-search to check if the graph contains a circle. If yes, it means "it is impossible to finish all courses".
