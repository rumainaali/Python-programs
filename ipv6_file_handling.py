'''
Date:22/05/2024
Multiple IPV6 Address validation using File Handling
'''

def is_Valid_hexa(ipv6_validation):
    ipv6_validation = ipv6_validation.strip()
    hexa = ipv6_validation.split(':')
    
    if len(hexa) != 8:
        print('Number of hexa must be 8')
        return
    
    for hexas in hexa:
        if not (len(hexas)>0 and len(hexas)<= 4):
            print('Length of each hexa must be greater than 0 and less than equal to 4')
            return
    
    valid_chars = 'abcdefABCDEF0123456789'
    ip = ''.join(hexa)
    for char in ip:
        if char not in valid_chars:
            print(f'{ipv6_validation} - Invalid ipv6 address')
            return

    print(f"{ipv6_validation} is a Valid ipv6 address")

f = open('ipv6_validation.txt')
for ipv in f:
    ipv6_validation = ipv.strip()
    is_Valid_hexa(ipv6_validation)
