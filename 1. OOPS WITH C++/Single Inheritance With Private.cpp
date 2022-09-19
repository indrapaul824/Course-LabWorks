#include <iostream>
#include <string.h>
using namespace std;
class stud
{
    int no;
    char name[20];
    public:
    	void getst()
    	{
    	    cout<<"\n\tNo: ";
    	    cin>>no;
    	    cout<<"\n\t Name:";
    	    cin>>name;
    	}
    	void dispst()
    	{
    	    cout<<"\n\tNo"<<no;
    	    cout<<"\n\tName"<<name;
    	}
};

class mark:public stud
{
    int m1,m2,m3;
    public: 
    	void getmk()
   		{
   		    getst();
    	    cout<<"\n\t 3 Marks";
    	    cin>>m1;
    	    cin>>m2;
    	    cin>>m3;
    	}
    	void dispmk()
    	{
    	    dispst();
    	    cout<<"\n\tm1:"<<m1<<"\n\tm2:"<<m2<<"\n\tm3:"<<m3;  	  
    	}
};

int main()
{
    mark obj;
    obj.getmk();
    obj.dispmk();
    return 0;
}

