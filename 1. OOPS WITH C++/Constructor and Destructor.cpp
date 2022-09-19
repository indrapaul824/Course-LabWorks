#include<iostream>
#include<string.h>
using namespace std;

class personal
{
	private:
		char name[20];
		int age;
		
	public:

	
		personal()
		{
			strcpy(name,"Ram");
			age=21;
		}
		personal(char n[20],int a)
		{
			strcpy(name,n);
			age=a;			
		}
		
		personal(const personal &q)
		{
			strcpy(name,q.name);
			age=q.age;
		}
		void display()
		{
			cout<<"The name is: "<<name;
			cout<<"The age is: "<<age;
		}
	~personal()
	{
		cout<<"\n\t Destructor Called";
	}
	
};

personal get()
{
	personal a("Maya",23);
	return a;
}

int main()
{
	personal p1;
	
	personal p2("Indra",19);

	personal p3(p2);
	
	personal p4=get();
	
	personal p5(p4);
	
	p1.display();
	return 0;
	
}
