#include<stdio.h>
#include<stdlib.h>

 int n;

 int linear(int x[], int value)
 {
    int i;
    for(i = 0; i < n; i++)
    {
        if(x[i] == value)
        {
            printf("%d was found at position %d of the array.\n", value, i);
            return 1;
        }
    }
    printf("Invalid Search!\n%d is not in the array.\n", value);
    return 1;
 }

 int binary(int x[], int value)
 {
    int low = 0, high = n - 1, mid;
    while(low <= high)
    {
        mid = (low + high) / 2;
        if(x[mid] == value)
        {
            printf("%d was found at position %d of the array.\n", value, mid);
            return 1;
        }
        else if(value < x[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    printf("Invalid Search!\n%d is not in the array.\n", value);
    return 1;
 }

 int main()
 {
    int i, search;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter array elements:\n");
    for(i = 0; i < n; i++)
    {
        printf("a[%d]: ", i);
        scanf("%d", &a[i]);
    }
    printf("Enter elements to search(linear): ");
    scanf("%d",&search);
    linear(a,search);
    printf("\n\n");
    printf("Enter elements to search(binary): ");
    scanf("%d",&search);
    binary(a,search);
    system("pause");
    return 0;
 }
