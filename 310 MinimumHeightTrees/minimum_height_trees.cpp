#include "minimum_height_trees.h"
#include <iostream>
#include <algorithm>

int findMinHeightTrees(int n, vector<pair<int, int>>& edges);
{
    unordered_map<int, unordered_set<int>> tree;

    if(n == 1) return vector<int>(1, 0);
    for(auto & p : edges)
    {
        tree[p.first].insert(p.second);
        tree[p.second].insert(p.first);
    }
    vector<int> leaves;

    for(auto & n : tree)
    {
        if(n.second.size() == 1)
            leaves.push_back(n.first);
    }

    while(n > 2)
    {
        n -= leaves.size();
        vector<int> new_leaves;
        for(int i : leaves)
        {
            int node = *(tree[i].begin());
            tree[i].erase(node);
            tree[node].erase(i);

            if(tree[node].size() == 1)
                new_leaves.push_back(node);
        }
        leaves = new_leaves;

    }
    return leaves;
}
}
