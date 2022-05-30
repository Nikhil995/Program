#two list into dictionary
l=input("enter the spsce saperated list1:")
l2=input("enter the spsce saperated list2:")
l2=l2.split()
l=l.split()
e=0
d={}
if len(l2)>len(l):
    for i in l:
        d[i]=l[e]
        e+=1
    for i in range(e,len(l2)):
        d[l2[i]]=0
else:
    for i in l2:
        d[i]=l2[e]
        e+=1
    for i in range(e,len(l)):
        d[l[i]]=0
print(d)