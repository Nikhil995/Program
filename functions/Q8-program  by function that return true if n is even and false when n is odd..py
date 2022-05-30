#program  by function that return true if n is even and false when n is odd.
def even(n):
    if n%2==0:
        return "True"
    else:
        return "False"
n=int(input())
a=even(n)
print(a)