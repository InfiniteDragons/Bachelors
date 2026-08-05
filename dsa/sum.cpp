// sum of natural no.

#include<stdio.h>
#include<stdlib.h>

 int recurse(int a)
 {
    if (a <= 1)
        return a;
    else
        return a + recurse(a - 1);
 }

 int main()
 {
    int n ,x;
    printf("Enter number of terms : ");
    scanf("%d",&n);
    x = recurse(n);
    printf("\nSum of %d natural numbers is %d\n", n, x);
    printf("\n\n");
    system("pause");
    return 0;
 }
