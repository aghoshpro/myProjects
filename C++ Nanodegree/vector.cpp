#include <iostream>
#include <vector>
using std::vector;
using std::cout;
int main() {
    // Declare and initialize a vector v here.
    vector<int> v{6,7,8};

    for(int i : v)
        cout << i << " ";
    cout << "\n";

    // Creating a 1D vector.
    vector<int> a = {0, 1, 2, 3, 4};

    cout << a[0];
    cout << a[1];
    cout << a[2];
    cout << "\n";

    // OR

    for(int i : a)
        cout << i << " ";
    cout << "\n";

    // Creating a 2D vector.
    vector<vector<int>> v2{{1,2}, {3,4}};
    cout << "Great! A 2D vector has been created." << "\n";
}