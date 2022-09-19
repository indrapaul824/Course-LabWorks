#include<iostream>
using namespace std;
class stud2;
class stud1
{
	public:
		int a=10;
		friend void display(stud1,stud2);
};

class stud2
{
	public:
		int b=20;
		friend void display(stud1,stud2);
};

void display(stud1 o,stud2 p)
{
	cout<<"a is "<<o.a<<"\n";
	cout<<"b is "<<p.b<<"\n";
}

int main()
{
	stud1 s1;
	stud2 s2;
	display(s1,s2);
	return 0;
}
