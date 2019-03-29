#include <vector>
#include <iostream>
#include <string>

using std::vector;
using std::string;

class Solution {
    public:
        bool exist(vector<vector<char>>& board, string word) {
            if(board.size() == 0) return false;

            for ( int i = 0; i < board.size(); ++i)
            {
                for( int j = 0; j < board[0].size(); ++j) 
                {
                    if (exist(board, word, 0, i, j)) return true;
                }
            }
            return false;
        }

    private:
        bool exist(vector<vector<char>>& board, string& word, int w, int i, int j) {
            if ( w >= word.size()) return true;
            if ( i >= board.size() || j >= board[0].size() ) return false;
            bool ret = false;
            char tmp;
            if(board[i][j] == word[w] && board[i][j] != '\0')
            {
                tmp = board[i][j]; 
                board[i][j] = '\0';
                ret = exist(board, word, w+1, i, j-1) || exist(board, word, w+1, i + 1, j) || exist(board, word, w+1, i, j+1) || exist(board, word, w+1, i - 1, j);
                board[i][j] = tmp;
            }

            return ret;
        }
};

int main() 
{
    return 0;
}
