#include<stdio.h>
 
 struct student
 {
    char name[20];
    float marks;
 };

 void main()
 {
    float avg;
    struct student s1,s2,s3;
    printf("Enter student info:\n");
    scanf("%s%f",s1.name,&s1.marks);
    scanf("%s%f",s2.name,&s2.marks);
    scanf("%s%f",s3.name,&s3.marks);
    avg = (s1.marks + s2.marks + s3.marks)/3;
    printf("avg = %.2f",avg);
 }
 