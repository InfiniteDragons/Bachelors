#include<stdio.h>

 void main()
 {
    int x;
    printf("Enter a number: ");
    scanf("%d",&x);
    palindrome(x);
 }

 void palindrome(int n)
 {
    int r,sum=0,temp;
    temp=n;
    while (n>0)
    {
        r=n%10;
        sum=(sum*10)+r;
        n=n/10;
    }
    if (temp==sum)
    {
        printf("%d is a palindrome number",temp);
    }
    else
    {
        printf("%d is not a palindrome number",temp);
    }
 }