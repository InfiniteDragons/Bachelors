#include<stdio.h>
#include<stdlib.h>

 struct node
 {
    int data;
    struct node *next;
    struct node *prev;
 };

 void display(struct node *head)
 {
    struct node *temp = head;
    printf("\nDoubly Linked List:\n");
    while(temp != NULL)
    {
        printf("| %p | %d | %p |\n",
               (void*)temp->prev,
               temp->data,
               (void*)temp->next);
        temp = temp->next;
    }
 }

 struct node* insertBeginning(struct node *head, int value)
 {
    struct node *newnode;
    newnode = (struct node*)malloc(sizeof(struct node));
    if(newnode == NULL)
    {
        printf("Memory allocation failed!\n");
        return head;
    }   
    newnode->data = value;
    newnode->next = head;
    newnode->prev = NULL;
    if(head != NULL)
        head->prev = newnode;
    head = newnode;
    return head;
 }

 struct node* insertEnd(struct node *head, int value)
 {
    struct node *newnode, *temp;
    newnode = (struct node*)malloc(sizeof(struct node));
    if(newnode == NULL)
    {
        printf("Memory allocation failed!\n");
        return head;
    }
    newnode->data = value;
    newnode->next = NULL;
    newnode->prev = NULL;
    if(head == NULL)
        return newnode;
    temp = head;
    while(temp->next != NULL)
        temp = temp->next;
    temp->next = newnode;
    newnode->prev = temp;
    return head;
 }

 struct node* insertMiddle(struct node *head, int value, int pos)
 {
    struct node *newnode, *temp;
    int i;
    if(pos == 1)
        return insertBeginning(head, value);
    temp = head;
    for(i = 1; i < pos - 1 && temp != NULL; i++)
        temp = temp->next;
    if(temp == NULL)
    {
        printf("Invalid Position!\n");
        return head;
    }
    newnode = (struct node*)malloc(sizeof(struct node));
    if(newnode == NULL)
    {
        printf("Memory Allocation Failed!\n");
        return head;
    }
    newnode->data = value;
    newnode->next = temp->next;
    newnode->prev = temp;
    if(temp->next != NULL)
        temp->next->prev = newnode;
    temp->next = newnode;
    printf("Node Inserted Successfully!\n");
    return head;
 }

 struct node* deleteBeginning(struct node *head)
 {
    struct node *temp;
    if(head == NULL)
    {
        printf("List Empty!\n");
        return NULL;
    }
    temp = head;
    head = head->next;
    if(head != NULL)
        head->prev = NULL;
    free(temp);
    return head;
 }

 struct node* deleteEnd(struct node *head)
 {
    struct node *temp;
    if(head == NULL)
    {
        printf("List Empty!\n");
        return NULL;
    }
    if(head->next == NULL)
    {
        free(head);
        return NULL;
    }
    temp = head;
    while(temp->next != NULL)
        temp = temp->next;
    temp->prev->next = NULL;
    free(temp);
    printf("Last Node Deleted Successfully!\n");
    return head;
 }

 struct node* deleteMiddle(struct node *head, int pos)
 {
    struct node *temp;
    int i;
    if(head == NULL)
    {
        printf("List Empty!\n");
        return NULL;
    }
    if(pos == 1)
        return deleteBeginning(head);
    temp = head;
    for(i = 1; i < pos && temp != NULL; i++)
        temp = temp->next;
    if(temp == NULL)
    {
        printf("Invalid Position!\n");
        return head;
    }
    if(temp->next == NULL)
    {
        printf("Use Delete End for the last node!\n");
        return head;
    }
    temp->prev->next = temp->next;
    temp->next->prev = temp->prev;
    free(temp);
    printf("Middle Node Deleted Successfully!\n");
    return head;
 }

 struct node* updateBeginning(struct node *head, int value)
 {
    if(head == NULL)
    {
        printf("List Empty!\n");
        return head;
    }
    head->data = value;
    printf("Beginning Node Updated Successfully!\n");
    return head;
 }

 struct node* updateMiddle(struct node *head, int value, int pos)
 {
    struct node *temp;
    int i;
    if(head == NULL)
    {
        printf("List Empty!\n");
        return head;
    }
    if(pos == 1)
    {
        printf("Use Update Beginning for position 1.\n");
        return head;
    }
    temp = head;
    for(i = 1; i < pos && temp != NULL; i++)
        temp = temp->next;
    if(temp == NULL || temp->next == NULL || temp->prev == NULL)
    {
        printf("Invalid Middle Position!\n");
        return head;
    }
    temp->data = value;
    printf("Middle Node Updated Successfully!\n");
    return head;
 }

 struct node* updateEnd(struct node *head, int value)
 {
    struct node *temp;
    if(head == NULL)
    {
        printf("List Empty!\n");
        return head;
    }
    temp = head;
    while(temp->next != NULL)
        temp = temp->next;
    temp->data = value;
    printf("Last Node Updated Successfully!\n");
    return head;
 }

 int main()
 {
    int choice, value, pos;
    struct node *head;
    head = (struct node*)malloc(sizeof(struct node));
    head->data = 10;
    head->next = NULL;
    head->prev = NULL;
    printf("Initial List:");
    display(head);

    while(1)
    {
        printf("\n Doubly Linked List \n 1. Insert at Beginning\n 2. Insert at Middle\n 3. Insert at End\n 4. Delete from Beginning\n ");
        printf("5. Delete from Middle\n 6. Delete from End\n 7. Update Beginning\n 8. Update Middle\n 9. Update End\n 10. Display\n 11. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter value: ");
                scanf("%d", &value);
                head = insertBeginning(head, value);
                break;

            case 2:
                printf("Enter value: ");
                scanf("%d", &value);
                printf("Enter position: ");
                scanf("%d", &pos);
                head = insertMiddle(head, value, pos);
                break;

            case 3:
                printf("Enter value: ");
                scanf("%d", &value);
                head = insertEnd(head, value);
                break;

            case 4:
                head = deleteBeginning(head);
                break;

            case 5:
                printf("Enter position: ");
                scanf("%d", &pos);
                head = deleteMiddle(head, pos);
                break;

            case 6:
                head = deleteEnd(head);
                break;

            case 7:
                printf("Enter new value: ");
                scanf("%d", &value);
                head = updateBeginning(head, value);
                break;

            case 8:
                printf("Enter middle position: ");
                scanf("%d", &pos);
                printf("Enter new value: ");
                scanf("%d", &value);
                head = updateMiddle(head, value, pos);
                break;

            case 9:
                printf("Enter new value: ");
                scanf("%d", &value);
                head = updateEnd(head, value);
                break;

            case 10:
                display(head);
                break;

            case 11:
                printf("Program Ended.\n");
                exit(0);

            default:
                printf("Invalid Choice!\n");
        }
    }

    system("pause");
    return 0;
 }
