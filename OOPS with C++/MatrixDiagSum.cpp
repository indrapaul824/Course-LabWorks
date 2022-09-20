#include<iostream>
using namespace std;

int main()
{
	
	int A[3][3],B[3][3],C[3][3],sum=0;
	cout<<"Enter the 9 elements for the matrix A:\n";
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
			cin>>A[i][j];	
	}
	cout<<"The Original matrix A is: \n";
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
			cout<<A[i][j]<<"\t";
		cout<<"\n";	
	}
	
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
			if((i==j) || ((i==3&&j==0) && (i==0&&j==3)))
			{
				sum=sum+A[i][j];
			}
		}
				
	}
	cout<<"The sum of diagonal elements is: "<<sum;
	return 0;
}
