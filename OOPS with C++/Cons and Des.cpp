#include <iostream>
#include <string.h>
using namespace std;
class personal
{
    private:
    int age;
    char name[20];
    
    public:
    personal()
    {
        strcpy(name,"Ram");
        age=21;
    }
    personal(char n[], int a)
    {
        strcpy(name, n);
        age=a;
    }
    personal(const personal &t)
    {
        strcpy(name,t.name);
        age=t.age;
    }
    void display()
    {
        cout<<"\n\tName:"<<name<<"\n\t Age:"<<age;
    }

~personal()
{
    cout<<"\n\tDestructor called";
}
};
personal get()
{
    personal a("Maya",23);
    return a;
}
int main()
{
    personal p;
    personal p1("Suv",23);
    personal p2(p1);
    personal p4=get();
    personal p5(p4);
    p.display();
    return 0;
}
