#include<iostream>

using namespace std;

class Student
{
	
	public:
		
		int no;
		char name[25];
		void getstud()
		{
			cout<<"Enter rollno: ";
			cin>>no;
			cout<<"Enter name: ";
			cin>>name;
		}
		
		void show()
		{
			cout<<"\nThe name is: "<<name;
			cout<<"\nThe roll no is: "<<no;
		}
		
};

class Marks:public Student
{
	
	public:
		int m1,m2,m3;
		void getMarks()
		{
			cout<<"\nEnter the three marks: ";
			cin>>m1>>m2>>m3;
		}
		void showm()
		{
			cout<<"\nThe three marks are: "<<m1<<", "<<m2<<", "<<m3;
		}
};

class Result:public Marks
{public:
	
	float sum,r;
	void getFMarks()
	{
		cout<<"\nEnter the full marks: ";
		cin>>r;
	}
	void showr()
	{
		sum=m1+m2+m3;
		float res;
		res=(sum*100)/(3*r);
		cout<<"\nThe result is: "<<res;
	}
};

int main()
{
	Student s1;
	s1.getstud();
	
	Marks s2;
	s2.getMarks();
	
	Result s3;
	s3.getFMarks();
	
	s1.show();
	s2.showm();
	s3.showr();
	return 0;
}









