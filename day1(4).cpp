
//WAP to find net salary of employee with 10% government tax.

#include<iostream>
 using namespace std;

 void net(float salary)
 {
    float net;
    net = salary - (salary * 10/100);
    cout<<"Net salary of employee after government tax is Rs."<<net;
 }

 int main()
 {
    float salary;
    cout<<"Enter salary of employee: Rs.";
    cin>>salary;
    cout<<"Salary of employee before government is Rs."<<salary<<endl;
    net(salary);
    return 0;
 }