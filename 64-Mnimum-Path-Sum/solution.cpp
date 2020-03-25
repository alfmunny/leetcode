class Solution {
    public:
        int minPathSum(vector<vector<int>>& grid) {

            int m = grid.size();
            int n = grid[0].size();

            vector<vector<int>> x(m, vector<int>(n, grid[0][0]));

            for (int i = 1; i < m; i++)
                x[i][0] = grid[i][0] + x[i-1][0];
            for (int i = 1; i < n; i++)
                x[0][i] = grid[0][i] + x[0][i-1];

            for (int i = 1; i < m; i++)
                for (int j = 1; j < n; j++)
                    x[i][j] = min(grid[i][j]+x[i-1][j], grid[i][j]+x[i][j-1]);

            return x[m-1][n-1];
        }

};
