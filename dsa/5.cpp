#include <stdio.h>

 void main()
 {
    int i,j,k;
    int a=1,b=7;

    for (i=1; i<5; i++)
    {
        for (j=0; j<i; j++)
        {
            printf("\t");
        }
        
        for (k = a; k<=b; k++)
        {
            printf("%d\t",k);
        }
        a++;
        b--;
        printf("\n");
    }
 }
