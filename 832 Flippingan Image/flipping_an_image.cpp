#include <iostream>
#include <vector>
using namespace std;


class FlippingImage {

public:
    vector< vector<int> > flippAndInvertImage(vector< vector<int> > &A) {
        int swap;
        int n;
        for ( int i = 0; i < A.size(); ++i ) {
            n = A[i].size();
            for ( int j = 0; j < A[i].size() / 2; ++j ) {
                swap = A[i][j];
                A[i][j] = 1 - A[i][n - j - 1];
                A[i][n - j - 1] = 1 - swap;
            }

            if ( n % 2 == 1 )
            {
                A[i][n/2] = 1 - A[i][n/2];
            }
        }
        return A;
    }
};


int main() {
    FlippingImage x;
    vector<int> a{1, 0, 0, 1, 0};
    vector<int> b{1, 0, 1, 1, 0};
    vector<int> c{1, 0, 0, 1, 1};
    vector<int> d{1, 0, 1, 1, 1};

    vector<vector<int>> matrix(4);


    matrix.push_back(a);
    matrix.push_back(b);
    matrix.push_back(c);
    matrix.push_back(d);

    for (auto i : matrix)
    {
        for (auto j : i)
            std::cout << j << " ";
        std::cout << endl;
    }

    x.flippAndInvertImage(matrix);


    for (auto i : matrix)
    {
        for (auto j : i)
            std::cout << j << " ";
        std::cout << endl;
    }
    return 0;
}
