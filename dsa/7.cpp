#include <stdio.h>
void main()
{
    int a[5],i,j,b[5],t;
    for ( i=0; i<5; i++)
    {
        printf("Enter a number: ");
        scanf("%d",&a[i]);
    }
    for ( i=0; i<5; i++)
    {
        for ( j=0; j<5; j++)
        {
            if (a[i]!=b[j])
            {
                b[i]=a[i];
            }
        }
    }
    for( i=0;i<5;i++)
    {
        printf("%d\t",b[i]);
    }
 }
 