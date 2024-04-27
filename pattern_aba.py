'''Date:20/04/2024
Problem #1
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba
'''

output = 'a'

for letter in 'bcdefg':
    output = output + letter + output
    print(output)
