#include<iostream>
using namespace std;
class Car
{
	public:
		int carno;
		int speed;
		char color[25];
		
		void move()
		{
			cout<<"\n Car started moving!";
			speed=speed+10;
		}
};

int main()
{
	Car c1;
	cout<<"\n Enter the car no.: ";
	cin>>c1.carno;
	c1.speed=0;
	cout<<"\n Enter the colour of the car: ";
	cin>>c1.color;
	
	cout<<"\nCar no.:"<<c1.carno<<"\nCar Colour:"<<c1.color<<"\nCar Speed: "<<c1.speed;
	cout<<"\nThe car was started!";
	
	c1.move();
	cout<<"\nCar Speed: "<<c1.speed;
	return 0;
	
}
