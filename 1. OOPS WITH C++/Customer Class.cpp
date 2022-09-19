#include<iostream>
using namespace std;
class cust
{
	public:
		char mobnum[12];
		char name[25];
		int dob,mob,yob;
		char add[50];
};
int main()
{
	cust c1;
	cout<<"Enter name of customer: \n";
	cin>>c1.name;
	cout<<"Enter mobile number of customer: \n";
	cin>>c1.mobnum;
	cout<<"Enter date, month and year of birth of customer: \n";
	cin>>c1.dob>>c1.mob>>c1.yob;
	cout<<"Enter address of customer: \n";
	cin>>c1.add;
	
	cout<<"Name: "<<c1.name<<"\n";
	cout<<"Mobile Number: "<<c1.mobnum<<"\n";
	cout<<"DOB: "<<c1.dob<<"/"<<c1.mob<<"/"<<c1.yob<<"\n";
	cout<<"Address: "<<c1.add;
}

