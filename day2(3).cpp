
// WAP to cube an integer, float and double number.

#include<iostream>
 using namespace std;
 
 void cube(int n);
 void cube(float n);
 void cube(double n);

 int main() {
     int a = 5;
     float b = 5.5f;
     double c = 6.7;
     cube(a); 
     cube(b); 
     cube(c); 
     return 0;
 }

void cube(int n) {
    cout << "Cube of int: " << (n*n*n) << endl;
}
void cube(float n) {
    cout << "Cube of float: " << (n*n*n) << endl;
}
void cube(double n) {
    cout << "Cube of double: " << (n*n*n) << endl;
}
