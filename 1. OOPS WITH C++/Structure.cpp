#include<iostream>
using namespace std;

struct Book
{
	int bno;
	char bt[20];
	
};

int main()
{
	struct Book b1,b2;
	cout<<"\n Enter book1 no.:";
	cin>>b1.bno;
	cout<<"\n Enter the book1 name:";
	cin>>b1.bt;
	
	cout<<"\n Enter book2 no.:";
	cin>>b2.bno;
	cout<<"\n Enter the book2 name:";
	cin>>b2.bt;
	
	cout<<"";
	return 0;
	
}
