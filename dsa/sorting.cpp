#include<stdio.h>
#include<stdlib.h>

 int n;

 int bubble(int x[])
 {
    int i, j, temp;
    for(i=0; i<n-1; i++)
    {
        for(j=0; j<n-i-1; j++)
        {
            if(x[j]>x[j+1])
            {
                temp = x[j];
                x[j] = x[j+1];
                x[j+1] = temp;
            }
        }
    }
    printf("\nBubble Sorted array:\n");
    for(i=0; i<n; i++)
        printf("%d\t", x[i]);
    printf("\n");
    return 1;
 }

 int insert(int x[])
 {
    int i, j, key;
    for(i=1; i<n; i++)
    {
        key = x[i];
        j = i-1;
        while(j>= 0 && x[j]>key)
        {
            x[j+1] = x[j];
            j--;
        }
        x[j+1] = key;
    }
    printf("\nInsert Sorted array:\n");
    for(i=0; i<n; i++)
        printf("%d\t", x[i]);
    printf("\n");
    return 1;
 }

 int quick(int x[], int low, int high)
 {
    int i=low, j=high;
    int pivot = x[(low+high)/2];
    int temp;
    while(i <= j)
    {
        while(x[i] < pivot)
            i++;
        while(x[j] > pivot)
            j--;
        if(i <= j)
        {
            temp = x[i];
            x[i] = x[j];
            x[j] = temp;
            i++;
            j--;
        }
    }
    if(low < j)
        quick(x, low, j);
    if(i < high)
        quick(x, i, high);
    return 1;
 }

 int main()
 {
    int i;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    int a[n];
    int b[n];
    int c[n];
    printf("Enter array elements:\n");
    for(i = 0; i < n; i++)
    {
        printf("a[%d]: ", i);
        scanf("%d", &a[i]);
        b[i] = a[i];
        c[i] = a[i];
    }
    bubble(a);
    printf("\n\n");
    insert(b);
    printf("\n\n");
    quick(c, 0, n-1);
    printf("\nQuick Sorted array:\n");
    for(i=0; i<n; i++)
        printf("%d\t", c[i]);
    printf("\n\n");
    system("pause");
    return 0;
 }
