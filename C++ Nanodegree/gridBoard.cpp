#include <sstream>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::ifstream;
using std::istringstream;
using std::string;
using std::vector;

// ------------------------------------------------

vector<int> ParseLine(string line) {
    istringstream sline(line);
    int n;
    char c;
    vector<int> row;
    while (sline >> n >> c && c == ',') {
      row.push_back(n);
    }
    return row;
}

vector<vector<int>> ReadBoardFile(string path) {
  ifstream myfile (path);
  if (myfile) {
    string line;
    while (getline(myfile, line)) {
      cout << line << "\n";
    }
  }
}

void PrintBoard(const vector<vector<int>> board) {
// PRINTING THE BOARD using for loop
cout << "\n-THE BOARD-\n\n";

  for (int row = 0; row < board.size(); row++) {
    for (int col = 0; col < board[0].size(); col++) {
      cout << board[row][col] << " ";
    }
    cout << "\n";
  }
  cout << "\n";
}

// ------------------------------------------------
// #include "test.cpp"
// ------------------------------------------------
int main() {
//   vector<vector<int>> board{{0, 1, 0, 0, 0, 0},
//                             {0, 1, 0, 0, 0, 0},
//                             {0, 1, 0, 0, 0, 0},
//                             {0, 1, 0, 0, 0, 0},
//                             {0, 0, 0, 0, 1, 0}};    


// Calling Function
// board.push_back({7, 7, 7, 7, 7, 7});

// PrintBoard(board);

// ReadBoardFile("Board.txt");
auto boardFile = ReadBoardFile("Board.txt");
PrintBoard(boardFile);
}