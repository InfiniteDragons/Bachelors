#another code

import numpy as np
def input_matrix():
    n=int(input("Enter the number of variables: "))
    a=np.zeros((n,n+1))
    for i in range(n):
        for j in range(n+1):
            a[i][j]=float(input("Enter the coefficient of variable  "))
    return a

def guass_jordan():
    a=input_matrix()
    n=len(a)
    for i in range(n):
        a[i]=a[i]/a[i][i]
        for j in range(n):
            if j!=i:
                ratio=a[j][i]/a[i][i]
                for k in range(n+1):
                    a[j][k]=a[j][k]-ratio*a[i][k]
                    
    for i in range(n):
        for j in range(n+1):
            print(a[i][j],end=" ")
        print()


    print("The solution is: ")
    for i in range(n):
        print("x",i+1,"=",a[i][n])

if __name__=="__main__":
    guass_jordan()
 