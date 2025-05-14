
//WAP to generate prime numbers in given range.

#include<iostream>
 using namespace std;

 void generate(int x,int y)
 {
    int i, j, n=0;
    for(i=x; i<=y; i++)
    {
        n=0;
        for(j=1; j<=i; j++)
        {
            if(i%j==0)
                n++;
        }
        if(n==2)
            cout<<i<<"\t";
    }
 }

 int main()
 {
    int a, b;
    cout<<"Enter lower and upper ranges:"<<endl;
    cin>>a>>b;
    cout<<"Prime numbers in the range "<<a<<" to "<<b<<" are:"<<endl;
    generate(a,b);
    return 0;
 }