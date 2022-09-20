#include<iostream>
#include<string.h>
using namespace std;

class Book
{
	
	public:
		int c=0;
		int bno;
		char bt[10];
		char *btStock[]={"MazeRunner","DaVinciCode","LostKey","Origin","DeathCure"};
	
	
	void stock(char x[])
	{
		for(int i=0;i<5;i++)
		{
			if(btStock[i]==x[0])
			{
				c++;
				break;
			}				
		}
		if(c>0)
			cout<<"Book is in stock.";
		else
			cout<<"Book is not in stock.";		
	}	
};
int main()
{
	Book b1;
	cout<<"\n Enter the book number: ";
	cin>>b1.bno;
	cout<<"\n Enter the book name: ";
	cin>>b1.bt;
	cout<<"\n The book nuber is:"<<b1.bno;
	b1.stock(b1.bt);	
}


