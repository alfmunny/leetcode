#include <iostream>
#include <vector>

class CourseSchedule2 {
public:
	std::vector<int> findOrder(int numCourses, std::vector<std::pair<int, int>>& prerequisities) {

		std::vector<std::vector<int>> graph(numCourses);
		std::vector<int> mark(numCourses);
		std::vector<int> res = std::vector<int>();
		
		// a directed graph to save every vetex and it's adjescent vetex.
		for (auto item : prerequisities)
		{
			graph[item.first].push_back(item.second);
		}

		// loop through the graph
		for (size_t i = 0; i < graph.size(); i++)
		{
			std::vector<int> temp(numCourses);

			// if any vertex of the graph can't not be visited by vistiGraph, then return an empty vector
			if (!visitGraph(graph, i, mark, temp, res))
			{
				return std::vector<int>();
			}
		}
		return res;
		
	}

	bool visitGraph(const std::vector<std::vector<int>>& graph, int pos, std::vector<int>& mark, std::vector<int>& temp, std::vector<int>& res)
	/*
	A function to visit the graph
	Params:
		graph: the whole graph
		pos: the vertex to visit
		mark: an array to mark the visited vetices 
		temp: an temperory array to mark the vetices in a single visiting loop, to check if the graph contains a circle.
		res: the result vector.

	return:
		bool
	*/
	{
		// if the vertex has been visited, return true.
		if (mark[pos] == 1)
		{
			return true;
		}

		// if the vertex has no adjescent vetices, marked it as visited.
		else if (graph[pos].empty())
		{
			mark[pos] = 1;
			res.push_back(pos);
			return true;
		}

		// if the vertex has adjescent vetices
		else
		{
			// loop through all the adjescent vetices
			for (size_t i = 0; i < graph[pos].size(); i++)
			{
				// check if the graph contains a cycle.
				if (temp[graph[pos][i]] == 1) {
					return false;
				}
				else 
				{
					temp[graph[pos][i]] = 1;
					if (visitGraph(graph, graph[pos][i], mark, temp, res))
					{
						// if the vetex can be visited, then unmark its temporary mark
						// in order to check the cycle in the next loop.
						temp[graph[pos][i]] = 0;
						continue;
					}
					else
					{
						return false;
					}

				}

			// when all the adjescent vetices are checked without cycle, than mark it as visited.
			}
			mark[pos] = 1;
			res.push_back(pos);
			return true;
		}
	}
};


