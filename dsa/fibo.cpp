// fabonacci of any number

#include<stdio.h>
#include<stdlib.h>

 int recurse(int a)
 {
    if (a <= 1)
        return a;
    else
        return recurse(a - 1) + recurse(a - 2);
 }

 int main()
 {
    int n ,i;
    printf("Enter number of terms : ");
    scanf("%d",&n);
    printf("\nFibonacci series of %d terms is\n",n);
    for (i = 0; i < n; i++) 
    {
        printf("%d   ", recurse(i));
    }
    printf("\n\n");
    system("pause");
    return 0;
 }
