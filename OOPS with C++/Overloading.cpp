#include<iostream>
#include<string.h>
using namespace std;

class Student
{
	public:
		char name[25];
		int mobno;
		void getDetails()
		{
			cout<<"Enter the name: ";
			cin>>name;
			cout<<"\nEnter the mobile number: ";
			cin>>mobno;
		}
		
		void getDetails(int x,char n[25])
		{
			strcpy(name,n);
			mobno=x;
		}
		
		void show()
		{
			cout<<"\nThe name is: "<<name;
			cout<<"\nThe mobile number is: "<<mobno;
		}
};

int main()
{
	Student s1;
	s1.getDetails();
	s1.show();
	s1.getDetails(74309,"Indrashis");
	s1.show();
	return 0;
}
