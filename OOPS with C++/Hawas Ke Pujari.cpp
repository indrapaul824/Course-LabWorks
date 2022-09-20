#include<iostream>
using namespace std;
class Vagina;
class Penis{
    int psize;
    public:
        void enterdata(){
            cout<<"O bsdk, lund ka size inch me bakk : ";
            cin>>psize;
        }
    friend void Check_satisfaction(Penis, Vagina);
};

class Vagina{
    int vsize;
    public:
        void enterdata(){
            cout<<"oo laude, gharwali ki chut ka size bol inch me : ";
            cin>>vsize;
        }
    friend void Check_satisfaction(Penis, Vagina);
};

void Check_satisfaction(Penis a, Vagina b){
    if(a.psize == b.vsize)
        cout<<"Made for each other :D "<<endl;
    else if (a.psize < b.vsize)
        cout<<"Laude me dam nahi, chuut kaafi badi hai, bada lauda laao ...maja nahi aaraha!!! "<<endl;
    else
        cout<<"Aaaaahhhhh! nikaaal bahar laude...,kitna bada hai haraaamkhor, meri chuut fatt rahi hai "<<endl;
}

int main(){
    Penis p;
    Vagina v;
    p.enterdata();
    v.enterdata();
    Check_satisfaction(p,v);
    return 0;
}
