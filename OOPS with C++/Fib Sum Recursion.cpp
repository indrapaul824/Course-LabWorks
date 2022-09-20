#include<iostream>
using namespace std;
int fib(int);
int main()
{
	int a=0,b=1,c,l;
	cout<<"Enter a limit: ";
	cin>>l;
	cout<<fib(l);
	return 0;
}
int fib(int x)
{
	
	if(x<=1)
		return x;
	return fib(x-1)+fib(x-2);
}
		
