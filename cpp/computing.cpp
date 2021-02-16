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
    float timeDif = time / params.step;
    float xPlace, yPlace, velocity;
    for(float i = 0; i <= time; i+= timeDif)
    {
        xPlace = params.velocityX * i;
        yPlace = params.velocityY * i - (params.g * i * i / 2);
        velocity = sqrt(pow(params.velocityX, 2) + pow(params.velocityY - i * params.g, 2));
        cout << i << " " << xPlace << " " << yPlace << " " << velocity << endl; 
    }
    return 0;
}
