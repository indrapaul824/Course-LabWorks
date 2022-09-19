#include<iostream>
using namespace std;
class stud2;
class stud1
{
	public:
		int a;
		friend void display(stud1,stud2);
};

class stud2
{
	public:
		int b;
		friend void display(stud1,stud2);
};

void display(stud1 o,stud2 p)
{
	if(o.a>p.b)
		cout<<"The greater is: "<<o.a;
	else
		cout<<"The greater is: "<<p.b;
}

int main()
{
	stud1 s1;
	stud2 s2;
	cout<<"Enter the value of A: ";
	cin>>s1.a;
	cout<<"Enter the value of B: ";
	cin>>s2.b;
	display(s1,s2);
	return 0;
}
