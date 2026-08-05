// Infix to Postfix Conversion using Stack   a+b*c+d-e^f/g-h = abc*+d+ef^g/-h-

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define max 100

 int top = -1;
 char stack[max];

 void push(char value)
 {
    if (top == max-1)
        printf("Stack Overflow\n");
    else
    {
        top++;
        stack[top]=value; 
    }
 }

 char pop()
 {
    if (top == -1)
    {
        printf("Stack Underflow\n");
        return 0;
    }
    else
    {
        return stack[top--];
    }
 }

 char peek()
 {
    if (top>=0)
        return stack[top];
    return 0;
 }

 int precedence(char op)
 {
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    if (op == '^')
        return 3;
    return 0;
 }

 int isRightAssociative(char op)
 {
    return op == '^';
 }

 int main()
 {
    char a[max], b = 0, temp;
    printf("Enter an infix expression: ");
    scanf("%s", a);
    printf("Postfix Expression: ");

    int i, j;
    for (i=0; i<strlen(a); i++)
    {
        temp = a[i];
        
        if ((temp >= 'A' && temp <= 'Z') || (temp >= 'a' && temp <= 'z') || (temp >= '0' && temp <= '9'))
        {
            printf("%c", temp);
        }

        else if ( temp == '(')
        {
            push(temp);
        }

        else if (temp == ')')
        {
            while (top != -1 && peek() != '(')
                printf("%c", pop());
            if (top != -1 && peek() == '(')
                pop();
        }

        else
        {
            while (top != -1 &&   (   (isRightAssociative(temp) && precedence(peek()) > precedence(temp)) || 
                                    (!isRightAssociative(temp) && precedence(peek()) >= precedence(temp))  )  )
                printf("%c", pop());
            push(temp);
        }
    }

    while(top != -1)
        printf("%c", pop());

    printf("\n\n\n");
    system("pause");
    return 0;
 }
