#include <iostream>
#include <string.h>
using namespace std;
class one
{
	int age;
    string name;
    public:
    one(int iage, string iname)
    {
        age =iage;
        name =iname;
    }
    void display()
    {
        cout<<"\n\tName:\t"<<name<<endl<<"\n\tAge:\t"<<age;
    }
    friend void display1(one ob);
};
    void display1(one ob)
    {
        cout<<"\n\tName:\t"<<ob.name<<endl<<"\n\tAge:\t"<<ob.age;
    }
int main()
{
    one ob1(1,"abi");
    ob1.display();
    display1(ob1);
    return 0;
}

