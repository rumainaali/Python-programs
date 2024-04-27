'''Date:14/04/2024
Pattern: ULEF
'''

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
    
print_U()

def print_L():
     for rows in range(1,no_of_rows+1):
        for cols in range(1,no_of_cols+1):
            if cols==1 or rows==no_of_rows:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
     print('')

print_L()

def print_E():
     for rows in range(1,no_of_rows+1):
        for cols in range(1,no_of_cols+1):
            if rows==1 or cols==1 or rows==no_of_rows//2 or rows==no_of_rows:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
     print('')

print_E()

def print_F():
     for rows in range(1,no_of_rows+1):
        for cols in range(1,no_of_cols+1):
            if rows==1 or cols==1 or rows==no_of_rows//2:
                print('*',end='')
            else:
                print(' ',end='')
        print('')
     print('')

print_F()
