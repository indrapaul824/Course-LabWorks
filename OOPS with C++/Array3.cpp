#include<iostream>
using namespace std;
int Sum(int[]);

int main()
{
	
	int A[5];
	cout<<"Enter 5 elements for the array:\n";
	for(int i=0;i<5;i++)
		cin>>A[i];
	cout<<"The sum is: "<<Sum(A);
	return 0;
}
int Sum(int x[])
{
	int sum=0;
	for(int i=0;i<5;i++)
	{
		sum=sum+x[i];
	}
	return sum;
}
