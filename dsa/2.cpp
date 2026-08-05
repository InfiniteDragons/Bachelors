#include<stdio.h>

 void main()
 {
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    check(n);
 }

 void check(int x)
 {
    int i,count=0;
    for ( i=0; i<x; i++)
    {
        if (x%i==0)
        {
            count++;
        }
    }
    if (count==2)
    {
        printf("%d is a prime number",x);
    }
    else
    {
        printf("%d is not a prime number",x);
    }
 }