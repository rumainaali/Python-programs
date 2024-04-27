'''Date:19/04/2024
Pattern-RUMAINA
'''
def print_R():
    for rows in range(1,6):
        for cols in range(1,6):
            if rows==1 or cols==1 or rows==3 or (cols==5 and (rows==2 or rows==3 or rows==5)) or (cols==3 and rows==4):
                print('*',end="")
            else:
                print(' ',end="")
        print('')
    print('')

no_of_rows=int(input('Enter the number of rows:'))
no_of_cols=int(input('Enter the number of columns:'))
    
def print_U():
    for rows in range(1,no_of_rows+1):
        for cols in range(1,no_of_cols+1):
            if cols==1 or cols==no_of_cols or rows==no_of_rows:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
    print('')
  
                
def print_M():
    for rows in range(5):
        for cols in range(5):
            if rows==0 or cols==0 or cols==4 or (cols==2 and (rows==1 or rows==2)):
                print('*',end="")
            else:
                print(' ',end="")
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
      

print_R()
print_U()
print_M()
print_A()
print_I()
print_N()
print_A()
