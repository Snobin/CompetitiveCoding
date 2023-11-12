#include <iostream>
#include <vector>
using namespace std;

vector<vector<int> > zeroMatrix(vector<vector<int> > &matrix, int n, int m) {
    
    int row[n] = {0};
    int col[m] = {0}; 
    
    // Mark rows and columns containing zero
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (matrix[i][j] == 0) {
                row[i] = 1;
                col[j] = 1;
            }
        }
    }
    
    // Set entire row and column to zero
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (row[i] || col[j]) {
                matrix[i][j] = 0;
            }
        }
    }
    
    return matrix;
}
int main() {
    // Example matrix
    vector<vector<int> > matrix(3, vector<int>(3, 0));

    matrix[0][0] = 1;
    matrix[0][1] = 2;
    matrix[0][2] = 3;

    matrix[1][0] = 4;
    matrix[1][1] = 0;
    matrix[1][2] = 6;

    matrix[2][0] = 7;
    matrix[2][1] = 8;
    matrix[2][2] = 9;

    // Call the zeroMatrix function
    zeroMatrix(matrix, 3, 3);

    // Display the modified matrix
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
