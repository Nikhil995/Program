d={}
a=int(input("enter d1 no of elements:"))
while(a):
    c,b=eval(input("enter key,dictioinary"))
    d[c]=b
    c,b=0,0
    a-=1
for i in d:
    p=0
    for j in d:
        if d[i]==d[j]:
            p+=1
            if p>1:
                d[i]=0
print(d)