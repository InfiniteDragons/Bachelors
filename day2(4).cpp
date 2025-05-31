#include<iostream>
 using namespace std;
 
 int main()
 {
    int i, x, y, *p;
    p = new int[5];
    for(i=0; i<5; i++)
    {
        cout << "Enter element " << i+1 << ": ";
        cin >> p[i];
    }
    for(i=0; i<5; i++)
    {
        if(p[i]>p[i+1])
            x= p[i];
        if(p[i]<p[i+1])
            y= p[i];
    }
    cout << "The largest number is: " << x << endl;
    cout << "The smallest number is: " << y << endl;
    return 0;
 }