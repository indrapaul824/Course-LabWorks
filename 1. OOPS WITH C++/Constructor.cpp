#include<iostream>
#include<cstring>
using namespace std;

struct Student
{
	char name[20];
	int rollno;
	int marks;
	
	Student(char x[20],int y,int z)
	{
		strcpy(name,x);
		rollno=y;
		marks=z;
	}
};

int main()
{
	Student s1("Indrashis",46,46);
	cout<<s1.name<<" "<<s1.rollno<<" "<<s1.marks;
	
	return 0;
}
