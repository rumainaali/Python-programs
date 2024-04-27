n=int(input('Enter the number:'))
a=0
b=0
for i in range(n+1):
    c=a+b
    print('Fibonacci series:',c)
    a=b
    print('a=',a)
    b=c
    print('b=',b)
