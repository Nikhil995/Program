a=1
c=0
try:
    print(a/c)
except (EOFError,ZeroDivisionError):
    print('cannot divide')