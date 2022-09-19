#include<iostream>
using namespace std;
struct Employee
{
	char name[30];
	int RoomNo;
	double MobNo;
	char Dept[10];
	int age;
};
int main()
{
	struct Employee e1,e2;
	cout<<"\n Enter the name of employee 1:";
	cin>>e1.name;
	cout<<"\n Enter the Room No. of employee 1:";
	cin>>e1.RoomNo;
	cout<<"\n Enter the Mobile Number of employee 1:";
	cin>>e1.MobNo;
	cout<<"\n Enter the Department of employee 1:";
	cin>>e1.Dept;
	cout<<"\n Enter the age of employee 1:";
	cin>>e1.age;
	
	cout<<"\n Enter the name of employee 2:";
	cin>>e2.name;
	cout<<"\n Enter the Room No. of employee 2:";
	cin>>e2.RoomNo;
	cout<<"\n Enter the Mobile Number of employee 2:";
	cin>>e2.MobNo;
	cout<<"\n Enter the Department of employee 2:";
	cin>>e2.Dept;
	cout<<"\n Enter the age of employee 2:";
	cin>>e2.age;
	return 0;
}
