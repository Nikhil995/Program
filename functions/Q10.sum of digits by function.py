def sum(n):
    s=0
    for digit in n:
        s+=int(digit)
    return(s)
n=input()
print(sum(n))