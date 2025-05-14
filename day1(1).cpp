
//WAP to add two numbers.

#include<iostream>
 using namespace std;

 void sum(int x,int y)
 {
    int sum;
    sum = x + y;
    cout<<"Sum of "<<x<<" & "<<y<<" is "<<sum;
 }

 int main()
 {
    int a, b;
    cout<<"Enter two numbers to be added"<<endl;
    cin>>a>>b;
    sum(a,b);
    return 0;
 }
