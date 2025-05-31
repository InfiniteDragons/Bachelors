
//WAP to add numbers in class.

#include<iostream>
 using namespace std;

 class number
 {
    int a, b;
    public: void input()
            {
                int x, y;
                cout<<"Enter two numbers:\n";
                cin>>x>>y;
                a=x;
                b=y;
            }
            void sum()
            {
                int s = a + b;
                cout<<"Sum of "<<a<<" & "<<b<<" is "<<s;
            }
 };

 int main()
 {
    class number n;
    n.input();
    n.sum();
    return 0;
 }