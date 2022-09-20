#include<iostream>
using namespace std;

class Student
{
	private:
		char name[25];
		char regno[10];
		char mobno[11];
	public:
		void getData()
		{
			cout<<"Enter the name: ";
			cin>>name;
			cout<<"Enter the registration number: ";
			cin>>regno;
			cout<<"Enter the mobile number: ";
			cin>>mobno;
		}
	
		void displayData()
		{
			cout<<"The name is: "<<name<<"\n";
			cout<<"The Registration number is: "<<regno<<"\n";
			cout<<"The mobile number of the student is: "<<mobno<<"\n";
		}
};
int main()
{
	Student s[2];
	for(int i=1;i<=2;i++)
	{
		s[i].getData();
		s[i].displayData();
	}	
	return 0;
}
