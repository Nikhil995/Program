
import numpy as np
r,c=eval(input("Enter the row,coloum of matrix:"))
g=np.empty([r,c])
for i in range(0,r):
    for j in range(0,c):
        g[i][j]=int(input(f"enter {i},{j} element of matrix1:"))
g1=np.empty([r,c])
for i in range(0,r):
    for j in range(0,c):
        g1[i][j]=int(input(f"enter {i},{j} element of matrix2:"))
g3=np.empty([r,c])
for i in range(0,r):
    for j in range(0,c):
        g3[i][j]=g[i][j]*g1[i][j]
print(g3)