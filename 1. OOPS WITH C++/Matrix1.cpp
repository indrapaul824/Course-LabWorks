#include<iostream>
using namespace std;

int main()
{
	
	int A[3][3],B[3][3],C[3][3];
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
	cout<<"The Original matrix A is: \n";
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
			cout<<A[i][j]<<"\t";
		cout<<"\n";	
	}	
	cout<<"The Original matrix B is: \n";
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
			cout<<B[i][j]<<"\t";
		cout<<"\n";	
	}	
	
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
			C[i][j]=A[i][j]+B[i][j];	
	}
	
	cout<<"The Addition matrix C is: \n";
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
			cout<<C[i][j]<<"\t";
		cout<<"\n";	
	}	
	return 0;
}
