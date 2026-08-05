#include <stdio.h>

void main() 
{
    int a;
    int *b = &a;
    printf("Enter value of a: ");
    scanf("%d",&a);
    printf("value of a = %d\n",a);
    printf("value of &a = %d\n",&a);
    printf("value of *a = %p",b);
}
