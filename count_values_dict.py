''' Date:12/04/2024
Count the repeated elements present in the diction example, 
fruits_dict={'fruit1':'Apple', 'fruit2':'Banana', 'fruit3':'Orange', 'fruit4':'Apple', 
            'fruit5':'Banana'} 
Output: {'Apple':2, 'Banana':2}
'''

fruits_dict={}
n=int(input('Enter the number of elements:'))

#Get the input from the user to create dictionary
for i in range(n):
    fruit_no=input('Enter the fruit number(example mention fruit1,..):')
    fruit_name=input(f'Enter the fruit name of {fruit_no}:')
    fruits_dict[fruit_no]=fruit_name
print(f'\nThe original dictionary is:{fruits_dict}\n')

#empty dictionary to store the count of elements
count_dict={}

#Iterate through the values i.e elements present in 'fruits_dict' 
for value in fruits_dict.values():
    title_value=value.title()
#If the element is already present as a key, then increment the count by 1
    if value in count_dict:
        count_dict[title_value]+=1
        print(f'Already present:{count_dict}')
#If the element is not yet present as the key, assign it with  value 1
    else:
        count_dict[title_value]=1
        print(f'Initial:{count_dict}')
print(f'\nThe count dictionary is:{count_dict}')