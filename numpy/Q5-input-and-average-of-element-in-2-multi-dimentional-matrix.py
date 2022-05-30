import numpy as np
r,c=eval(input("enter row,column of the matrix:"))
arr=np.empty([r,c])
k=0
for i in range(0,r):
    for j in range(0,c):
        arr[i][j]=int(input(f"ENter the {i},{j} element of the matrix:"))
        k+=arr[i][j]
av=k/(r*c)
print("avg:",av)