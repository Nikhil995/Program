d={}
a=int(input("enter d1 no of elements:"))
while(a):
    c,b=eval(input("enter key,dictioinary"))
    d[c]=b
    c,b=0,0
    a-=1
max=0
for i in d:
    if d[i]>max:
        max=d[i]
min=max
for i in d:    
    if d[i]<min:
        min=d[i]
print(f"max={max},min={min}")  