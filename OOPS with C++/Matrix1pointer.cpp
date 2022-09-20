#include<iostream>
using namespace std;

int main()
{
	
	int A[3][3],B[3][3],C[3][3];
	int *p1,*p2,*p3;
	
	cout<<"Enter the 9 elements for the matrix A:\n";
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
			cin>>A[i][j];	
	}
	cout<<"Enter the 9 elements for the matrix b:\n";
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
			cin>>B[i][j];	
	}
	p1=&A[0][0];
	p2=&B[0][0];
	p3=&C[0][0];
	cout<<"The Original matrix A is: \n";
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++,p1++)
			cout<<*p1<<"\t";
		cout<<"\n";	
	}	
	cout<<"The Original matrix B is: \n";
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++,p2++)
			cout<<*p2<<"\t";
		cout<<"\n";	
	}	
	
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++,p1++,p2++,p3++)
		{
			*p3=*p1+*p2;
		}
		
	}

	cout<<"The Added matrix C is: \n";
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
			cout<<C[i][j]<<"\t";
		cout<<"\n";	
	}	
	return 0;
}
