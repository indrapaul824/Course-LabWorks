#include<iostream>
using namespace std;

class friends
{
	int no,rno;
	friend void display(friends);
};

void display(friends o)
{
	o.no=10;
	o.rno=20;
	cout<<"a ---> "<<o.no<<"\n";
	cout<<"b ---> "<<o.rno<<"\n";
}
int main()
{
	friends f;
	display(f);
	
	return 0;
}
