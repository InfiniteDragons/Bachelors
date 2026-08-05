#include<stdio.h>
#include<stdlib.h>

 int top = -1;
 int max = 5;
 int stack[5];

 int peek()
 {
    if (top>=0)
        printf("%d\n",stack[top]);
    return 1;
 }

 int push(int value)
 {
    if (top == max-1)
        printf("Stack Overflow\n");
    else
    {
        top++;
        stack[top]=value;
        
    }
    return 1;
 }

 int pop()
 {
    if (top == -1)
        printf("Stack Underflow\n");
    else
    {
        printf("%d is poped\n",stack[top]);
        top--;
        stack[top+1]=0;
    }
    return 1;
 }

 int display()
 {
    int i;
    printf("Stack is :\t");
    for (i=top;i>=0;i--)
        printf("%d\t",stack[i]);
    return 1;
 }

 int main()
 {
    int a,c,value;
    do
    {
        printf("Push(1) or Pop(2) or display(3) or peek(4)?: ");
        scanf("%d",&a);
        switch(a)
        {
            case 1: printf("Enter a number:");
			        scanf("%d",&value);
			        push(value);
                    break;
            case 2: pop();
                    break;
            case 3: display();
                    break;
            case 4: peek();
                    break;
            default: printf("Error input!!! Try again");
        }
        printf("\nDo you want to continue?(yes=1)");
        scanf("%d",&c);
    }while(c==1);
    system("pause");
    return 0;
 }
 