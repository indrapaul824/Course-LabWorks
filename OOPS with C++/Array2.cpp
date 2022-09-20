#include<iostream>
using namespace std;
int main()
{
int oa[10],ea[10],o=0,e=0;
int i,j,inp;

cout<<"\n Number of inputs:";
cin>>inp;

for(i=0;i<inp;i++)
{
cin>>j;
if(j%2==0)
{
ea[e]=j;e++;
}
else
{
oa[o]=j;o++;}
}
cout<<"\n ODD";
for(i=0;i<o;i++)
cout<<"\n"<<oa[i];
cout<<"\n Even";
for(i=0;i<e;i++)
cout<<"\n"<<ea[i];

return 0;
}
