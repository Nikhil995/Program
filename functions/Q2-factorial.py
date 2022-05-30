def factorial(num):
    fact = 1
    while(num!=0):
        fact *= num
        num = num - 1
    print("Factorial is",fact)
num = int(input("Enter number "))
factorial(num)