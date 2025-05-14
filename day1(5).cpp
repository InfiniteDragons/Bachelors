
//WAP to print character for given amount of times with default values.

#include<iostream>
 using namespace std;

 void display(char x='P',int y=5)
 {
    int i=1;
    do
    {
        cout<<x<<endl;
        i++;
    } while(i<=y);
 }
 
 int main()
 {
    char a;
    int n;
    cout<<"Enter character:"<<endl;
    cin>>a;
    cout<<"Enter number of times "<<a<<" is to be printed:"<<endl;
    cin>>n;
    display(a,n);
    cout<<"Using default value of n:"<<endl;
    display(a);
    cout<<"Using default values:"<<endl;
    display();
    return 0;
 }