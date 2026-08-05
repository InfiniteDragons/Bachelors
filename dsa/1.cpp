#include <stdio.h>
#include<conio.h>

 void swap(int x, int y);

 int main()
 {
    int a,b;
    printf("Enter two numbers:");
    scanf("%d%d",&a,&b);
    printf("Before swapping: %d\t %d\n",a,b);
    swap(a,b);
    return 0;
    getch();
 }

 void swap(int x, int y)
 {
    int t;
    t=x;
    x=y;
    y=t;
    printf("After swapping: %d \t%d",x,y);
 }
