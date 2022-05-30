a=int(input("enter the length of dict:"))
d={}
while(a):
    b,c=eval(input("enter key,value:"))
    d[b]=c
    a-=1
print(d)
a=int(input("Enter the key you want to remove:"))
d.pop(a)
print(f"Dict. after key removal:{d}")