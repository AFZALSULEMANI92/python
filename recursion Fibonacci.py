n=int(input('enter the number'))
def fib (n):
     if n==1:
          return n
     elif n==2:
          return 1
     else:
          return fib(n-1)+fib(n-2)
print(fib(n))    