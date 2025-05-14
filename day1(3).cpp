
//WAP to find volume of cube, rectriangle and cylinder using overload function.

#include<iostream>
#define pi 3.14
 using namespace std;

 void volume(int length)
 {
    int vol;
    vol = length * length * length;
    cout<<"Volume of cube is "<<vol<<endl;
 }

 void volume(int length,int breadth,int height)
 {
    int vol;
    vol = length * breadth * height;
    cout<<"Volume of rectangle is "<<vol<<endl;
 }

 void volume(int radius,int height)
 {
    float vol;
    vol = pi * float(radius) * float(radius) * float(height);
    cout<<"Volume of cylinder is "<<vol<<endl;
 }

 int main()
 {
    int l, b, h, length, height, r;
    cout<<"Enter parameters of cube:"<<endl;
    cin>>length;
    volume(length);
    cout<<"Enter parameters of rectangle:"<<endl;
    cin>>l>>b>>h;
    volume(l,b,h);
    cout<<"Enter parameters of cylinder:"<<endl;
    cin>>r>>height;
    volume(r,height);
    return 0;
 }