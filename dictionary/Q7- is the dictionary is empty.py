d={}
a=int(input("enter d1 no of elements:"))
while(a):
    c,b=eval(input("enter key,dictioinary"))
    d[c]=b
    c,b=0,0
    a-=1
if d == {}:
    print("YES")
else:
    print("NO")