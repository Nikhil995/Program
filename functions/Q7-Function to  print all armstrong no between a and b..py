#wap to  print all armstrong no between a and b.
def arm(a,n):
    i=a
    while i<=n:
        s=0
        c=0
        b=i
        k=i
        a=i
        while k:
            c=c+1
            k=k//10
        while a:
            r=a%10
            s=s+r**c
            a=a//10
        if s==b:
            print(s)
        i=i+1
a=int(input())
n=int(input())
arm(a,n)