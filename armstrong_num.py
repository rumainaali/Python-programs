'''Accept a number and find out if it is Armstrong number'''

num=int(input('Enter the number:'))
sum_num=0
temp=num
while temp>0:
    rem=temp%10
    print('Remainder:',rem)
    sum_num+=rem**3
    print('Sum of the cube of the digits:',sum_num)
    temp=temp//10
    print('Quotient:',temp)

if sum_num==num:
    print(f'Given {num} is Armstrong number')
else:
    print(f'Given {num} is not an Armstrong number')