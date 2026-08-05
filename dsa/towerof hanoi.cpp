//tower of hanoi

#include<stdio.h>
#include<stdlib.h>
#define max 5

 int top = -1;


 int tower(3,a,)
 {
    int a[max], b[max], c[max], temp;
    if (x == 1)
    {
        top++;
        c[top] = a[max-1];
    }
    else
    {
        top++;
        b[top] = a[max-2];
        for i 
        c = b;



    }
    return 0;
 }

 int main()
 {
    int n, i;
    printf("Enter number of disks: ");
    scanf("%d",&n);
    tower(n);
    system("pause");
    return 0;
 }


 #include<stdio.h>
#include<conio.h>
#include<math.h>
void toh(int n,char a,char b,char c)
{ if(n==1)
	{
		printf("move the disk 1 from %c to %c\n",a,c);
		return;
	}
	
	toh(n-1,a,c,b);
	printf("move the disk %d from %c to %c\n",n,a,c);
	toh(n-1,b,a,c);
	
	
}
int main()
{
	int x;
	printf("enter the number of disks:");
	scanf("%d",&x);
	int no_of_moves;
	no_of_moves=(pow(2,x))-1;
	printf("number of moves required is %d\n",no_of_moves);
	toh(x,'A','B','C');
	return 0;	
}
