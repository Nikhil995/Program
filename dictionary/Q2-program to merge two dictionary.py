#program to merge two dictionary
d={}
a=int(input("enter d1 no of elements:"))
while(a):
    c,b=eval(input("enter key,dictioinary"))
    d[c]=b
    c,b=0,0
    a-=1
d1={}
a=int(inpt("enter no of elements of d2:"))
while(a):
    c,b=eval(input("enter key,dictioinary"))
    d1[c]=b
    c,b=0,0
    a-=1

if len(d1)>len(d):
    for i in d1:
        d[i]=d1[i]
    print(d)
else:
      for i in d:
        d1[i]=d[i]
      print(d1)