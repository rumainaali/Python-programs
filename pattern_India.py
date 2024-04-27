'''Date:14/04/2024
Pattern : INDIA
'''

no_of_rows=int(input('Enter the number of rows:'))
no_of_cols=int(input('Enter the number of columns:'))

def print_I():
  if no_of_rows==no_of_cols or no_of_rows>no_of_cols:
    for row in range(1,no_of_rows+1):
        for col in range(1,no_of_cols+1):
            if row==1 or row==no_of_rows or col==no_of_cols//2:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    print('')
  else:
      print('Number of rows and cols must be same or number of rows must be greater than number of columns to print pattern I')

def print_N():
  if no_of_rows==no_of_cols:
    for rows in range(1,no_of_rows+1):
        for cols in range(1,no_of_cols+1):
            if cols==1 or cols==no_of_rows or cols==rows:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    print('')
  else:
      print('Number of rows and columns should be same to print pattern N')

def print_D():
    for row in range(1,no_of_rows+1):
        for col in range(1,no_of_cols+1):
            if row==1 or col==1 or row==no_of_rows or col==no_of_cols:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    print('')

def print_A():
    for rows in range(1,no_of_rows+1):
        for cols in range(1,no_of_cols+1):
            if rows==1 or cols==1 or cols==no_of_cols or rows==no_of_rows//2:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    print('')
    

print_I()
print_N()
print_D()
print_I()
print_A()
