a=int(input("enter the nth line:"))
file1=open('file.txt','r')
for i in range(0,a):
    print(file1.readline())