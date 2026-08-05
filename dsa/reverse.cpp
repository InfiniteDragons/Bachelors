// reverse natural no.

#include<stdio.h>
#include<stdlib.h>

 int reverse(int n)
 {
    if (n <= 0)
        return 0;
    printf("%d  ", n);
    reverse(n - 1);
    return 0;
 }

 int main()
 {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Natural numbers in reverse order:\n");
    reverse(n);
    printf("\n\n");
    system("pause");
    return 0;
 }
