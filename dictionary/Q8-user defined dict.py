n=int(input("enter no of terms"))
d={}
for i in range(n):
    a=input("enter key")
    b=input("enter value")
    d.update({a:b})
print(d)