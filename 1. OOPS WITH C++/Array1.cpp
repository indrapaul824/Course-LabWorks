#include<iostream>
using namespace std;
int main()
{
	int i,j;
	int A[10],B[10];
	cout<<"Enter the values:";
	for(i=0,j=0;i<6 && j<6;i++,j++)
	{
		cin>>A[i];
		cin>>B[j];
	}
	for(int i=0;i<5;i++)
	{
		cout<<A[i]<<" ";
	}
	cout<<"\n";
	for(int i=0;i<5;i++)
	{
		cout<<B[i]<<" ";
	}
	return 0;
}
