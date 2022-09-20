#include<iostream>
#include<string.h>
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
			cout<<"\n\tName: ";
			cin>>name;	
		}
		
		void dispst()
		{
			cout<<"\n\tNo.: "<<no;
			cout<<"\n\tName: "<<name;
		}
};

class Marks:public stud
{
	int m1,m2,m3;
	public:
		void getmk()
		{
			getst();
			cout<<"\n\tThree Marks:\n\t";
			cin>>m1;
			cout<<"\n\t";
			cin>>m2;
			cout<<"\n\t";
			cin>>m3;	
		}
		void dispmk()
		{
			dispst();
			cout<<"\n\tM1="<<m1<<"\n\tM2="<<m2<<"\n\tM3="<<m3;
		}
};

int main()
{
	Marks obj;	
	obj.getmk();
	obj.dispmk();
	return 0;
}




