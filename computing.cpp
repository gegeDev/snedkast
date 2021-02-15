#include <iostream>
#include <math.h>
using namespace std;
struct Settings
{
    float g;
    float hd;
    float step;
    float velocityY;
    float velocityX;
};
int main()
{
    Settings params;
    cin >> params.g >> params.hd >> params.step >> params.velocityY >> params.velocityX;
    float time = 2.0 * params.velocityY / params.g;
    cout << time << endl;
    float timeDef = time / params.step;
    for(float i = 0; i <= time; i+= timeDef)
    {
        float xPlace = params.velocityX * i;
        float yPlace = params.velocityY * i - (params.g * i * i / 2);
        cout << i << " " << xPlace << yPlace << endl; 
    }
    return 0;
}
