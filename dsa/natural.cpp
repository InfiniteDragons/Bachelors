// natural no.

#include<stdio.h>
#include<stdlib.h>

 int natural(int a)
 {
    if (a <= 0)
        return 0;
    natural(a - 1);
    printf("%d  ", a);
    return 0;
 }

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Natural numbers from 1 to %d are:\n", n);
    natural(n);
    printf("\n\n");
    system("pause");
    return 0;
}
