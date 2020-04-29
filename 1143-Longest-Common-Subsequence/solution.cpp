#include <iostream>
#include <string>

using namespace std;

class Solution {
  public:
    // brute force, recursive
    int LCS(string text1, string text2) {
      int M = text1.size();
      int N = text2.size();
      int ans = 0;

      for (size_t i = 0; i < M; i++) {
        for (size_t j = 0; j < N; j++) {
          if (text1[i] == text2[j]) {
            string t1 = text1.substr(0, i);
            string t2 = text2.substr(0, j);
            ans = LCS(t1, t2) + 1;
          } else {
            ans = max(LCS(text1.substr(0, i + 1), text2.substr(0, j)),
                LCS(text1.substr(0, i), text2.substr(0, j + 1)));
          }
        }
      }
      return ans;
    }

    // DP optimization
    int LCS2(string text1, string text2) {
      int M = text1.size();
      int N = text2.size();
      int dp[M + 1][N + 1];                           // padding
      memset(dp, 0, (M + 1) * (N + 1) * sizeof(int)); // initialization

      for (int i = 0; i < M; i++)
        for (int j = 0; j < N; j++) {
          if (text1[i] == text2[j])
            dp[i + 1][j + 1] = dp[i][j] + 1;
          else
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1]);
        }

      return dp[M][N];
    }
};

int main() {
  Solution sol;
  string text1 = "abcde";
  string text2 = "ace";
  cout << "recursive: " << sol.LCS(text1, text2) << endl;
  cout << "dp: " << sol.LCS2(text1, text2) << endl;
}
