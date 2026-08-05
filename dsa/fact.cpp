// fact of any number

#include<stdio.h>
#include<stdlib.h>

 int recurse(int a)
 {
    if (a == 0 || a == 1)
        return 1;
    else
        return a * recurse(a-1);
 }

 int main()
 {
    int n, x;
    printf("Enter a number : ");
    scanf("%d",&n);
    x = recurse(n);
    printf("\nFactorial of %d is %d.\n\n",n ,x);
    system("pause");
    return 0;
 }
