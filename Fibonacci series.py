# Fibonacci series in python

s=int(input("How many terms? \n"))

def fib(s):

    a = 0
    b = 1

    if s == 1:
        print(a)

    else:
        print("Fibonacci sequence for",s,"is:")
        print(a)
        print(b)

    for i in range(2,s):
        c = a + b
        a = b
        b = c
        print(a+b)

fib(s)




