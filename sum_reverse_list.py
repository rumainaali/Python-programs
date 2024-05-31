'''Date:28/05/2024
Add two number represented in a list as reversed. print the sum also as a list in reverse order
eg input list1 = [1,2,3] list2 = [5,6,7]
answer= [6,8,0,1]
 explanation (321 + 765 = 1086)
'''
l1=[1,2,3]
l2=[5,6,7]

new_l1=[]
for i in l1:
    new_l1.insert(0,i)
print(f'Reversed list l1:\n{new_l1}')

new_l2=[]
for i in l2:
    new_l2.insert(0,i)
print(f'Reversed list l2:\n{new_l2}')

l1_str=map(str,new_l1)
l1=list(l1_str)
print(f'Integers of list l1 is coverted to string:\n{l1}')

l1_join=''.join(l1)
print(f'List l1 elements joined:\n{l1_join}')

l2_str=map(str,new_l2)
l2=list(l2_str)
print(f'Integers of list l2 is coverted to string:\n{l2}')

l2_join=''.join(l2)
print(f'List l2 elements joined:\n{l2_join}')

sum=0

l1_int=int(l1_join)
l2_int=int(l2_join)
sum=l1_int+l2_int
print(f'sum of numbers:\n{sum}')

sum_str=str(sum)
sum_list_reverse=[]
for value in sum_str:
    sum_list_reverse.insert(0,value)
print(f'Sum of lists reversed:\n{sum_list_reverse}')
