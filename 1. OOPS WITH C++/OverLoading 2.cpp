#include <iostream>
using namespace std;
class add
{
    public:
    void sum()
    {
        cout<<"Total=0";
    }
    void sum(int a,int b,int c=0, int d=0)
    {
        int t;
        t=a+b+c+d;
        cout<<"\n\t Total:"<<t;
    }
};
int main()
{
    add ao;
    ao.sum();
    ao.sum(2,3);
    ao.sum(2,3,4);
    ao.sum(2,3,4,5);
    return 0;
}

