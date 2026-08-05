#include<stdio.h>
#include<stdlib.h>
#define max 5

 int front = -1, rear = -1;
 int queue[5];

 int isempty()
 {
   if (front == -1 && rear == -1)
      return 1;
   else if (front == rear + 1)
      return 1;
   else
      return 0;
 }

 int isfull()
 {
   if (rear == max - 1)
      return 1;
   else
      return 0;
 }

 int enqueue(int value)
 {
   if (isfull())
      printf("Queue is full\n");
   else
   {
      rear = (rear + 1) % max;
      queue[rear] = value;
      if (front == -1)
         front = 0;
   }
   printf("%d is enqueued\n", value);
   return 1;
 }

 int dequeue()
 {
   if (isempty())
      printf("Queue is empty\n");
   else
   {
      printf("%d is dequeued\n", queue[front]);
      front++;
      if (front >= rear)
      {
         front = -1;
         rear = -1;
      }
   }
   return 1;
 }

 int search()
 {
   if (isempty())
      printf("Queue is empty\n");
   else
   {
      int value, i, check=0;
      printf("Enter a number to search:");
      scanf("%d", &value);
      for (i = front; i <= rear; i++)
      {
         if (queue[i] == value)
         {
            printf("%d is found at position %d\n", value, i + 1);
            check++;
            break;
         }
         if (i == rear && check == 0)
            printf("%d is not found in the queue\n", value);
      }
   }
   return 1;
 }

 int display()
 {
   int i;
   if (isempty())
     printf("Queue is empty\n");
   else
   {
      printf("Queue is :\t");
      for (i = front; i <= rear; i++)
         printf("%d\t", queue[i]);
   }
   printf("\n");
   return 1;
 }

 int main()
 {
   int a,c,value;
   do
   {
      printf("Enqueue(1) or Dequeue(2) or Display(3) or Search(4)?: ");
      scanf("%d",&a);
      switch(a)
      {
         case 1: printf("Enter a number:");
		           scanf("%d",&value);
		           enqueue(value);
                 break;
         case 2: dequeue();
                 break;
         case 3: display();
                 break;
         case 4: search();
                 break;
         default: printf("Error input!!! Try again");
      }
      printf("\nDo you want to continue?(yes=1)");
      scanf("%d",&c);
   }while(c==1);
   system("pause");
   return 0;
 }
 