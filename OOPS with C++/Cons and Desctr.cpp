//Employee Details: Single
#include <iostream>
using namespace std;
class employee
{
    public:
    int Rno;
    char name[20];
    float salary;
    
    void get()
    {
        cout<<"\n\t Enter Rno:";
        cin>>Rno;
        cout<<"\n\t Enter Name:";
        cin>>name;
        cout<<"\n\t Salary:";
        cin>>salary;
    }
        void put()
        {
            cout<<"\t\n"<<Rno<<"\t\n"<<name<<"\t\n"<<salary;
        }
    };

int main()
{
    employee e;
    e.get();
    e.put();
}
//Multiple Employee

#include <iostream>
using namespace std;
class employee
{
    int Rno;
    char name[20];
    float salary;
    public:
    void get()
    {
        cout<<"\n\t Enter Rno:";
        cin>>Rno;
        cout<<"\n\t Enter Name:";
        cin>>name;
        cout<<"\n\t Salary:";
        cin>>salary;
    }
        void put()
        {
            cout<<"\t\n"<<Rno<<"\t\n"<<name<<"\t\n"<<salary;
        }
    };

int main()
{
    int i; 
    employee e[3];
    for(i=1;i<=3;i++)
    {
        cout<<"\n\t Enter employee "<<i <<"data";
        e[i].get();
    }
    for(i=1;i<=3;i++)
    {
        cout<<"\n\t Enter employee "<<i <<"data";
        e[i].put();
}
return 0;
}
