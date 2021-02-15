#include <iostream>
using namespace std;
struct Settings
{
    int g;
    int hd;
};
int main()
{
    Settings params;
    cin >> params.g >> params.hd;
    cout << params.g << " " << params.hd << endl;
    return 0;
}
