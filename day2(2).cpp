
//WAP to find area & parameter of 5 cubes.

#include<iostream>
 using namespace std;

 class cube
 {
    int length;
    public: void input()
            {
                int l;
                cout<<"Enter lenght of cube: ";
                cin>>l;
                length=l;
            }
            void info()
            {
                int area, parameter;
                area = length*length;
                parameter = 2*length;
                cout<<"Area of cube is "<<area<<endl;
                cout<<"Parameter of cube is "<<parameter<<endl;
            }
 };

 int main()
 {
    class cube c1,c2,c3,c4,c5;
    c1.input();
    c1.info();
    cout<<"\n\n";
    c2.input();
    c2.info();
    cout<<"\n\n";
    c3.input();
    c3.info();
    cout<<"\n\n";
    c4.input();
    c4.info();
    cout<<"\n\n";
    c5.input();
    c5.info();
    cout<<"\n\n";
    return 0;
 }