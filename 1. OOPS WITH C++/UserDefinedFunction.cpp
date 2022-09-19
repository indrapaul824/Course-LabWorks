#include<iostream>
using namespace std;
int add(int x, int y)
{
	return (x+y);
}
int sub(int x, int y)
{
	return (x-y);
}
int prod(int x, int y)
{
	return (x*y);
}
int div(int x, int y)
{
	return (x/y);
}
int main()
{
	int f,a,b;
	cout<<"Options: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n";
	cin>>f;
	cout<<"Enter the numbers:\n";
	cin>>a>>b;
	if(f==1)
		cout<<add(a,b);
	else if(f==2)
		cout<<sub(a,b);
	else if(f==3)
		cout<<prod(a,b);
	else
		cout<<div(a,b);
	return 0;
	
}
