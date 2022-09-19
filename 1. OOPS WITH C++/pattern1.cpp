#include<iostream>
using namespace std;
int main()
{
	int l,j;
	cout<<"Enter the limit:\n";
	cin>>l;
	for(int i=0;i<l;i++)
	{
		int space=l;
		for(int k=space-i;k>=1;k--)
		{
			cout<<" ";
		}
		for(j=1;j<=i;j++)
	    {
		 	cout<<j;
		}
		for(int m=j;m>=1;m--)
		{
			cout<<m;
		}
	    cout<<"\n";
	}
	return 0;
}
