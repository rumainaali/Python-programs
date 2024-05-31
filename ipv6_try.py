'''
Date:22/05/2024
Multiple IPV6 Address validation using File Handling and try, except concept
'''

def is_Valid_hexa(ipv6_validation):
    try:
        ipv6_validation = ipv6_validation.strip()
        hexa = ipv6_validation.split(':')
        ipv6 = ''.join(hexa)
        
        if len(hexa) != 8:
            print(f'{ipv6_validation} - Number of hexa must be 8')
            return
        
        for hexas in hexa:
            if not (len(hexas)>0 and len(hexas)<= 4):
                print(f'{ipv6_validation} - Length of each hexa must be greater than 0 and less than equal to 4')
                return
        
        valid_chars = 'abcdefABCDEF0123456789'
        for char in ipv6:
            if char not in valid_chars:
                print(f'{ipv6_validation} - Invalid ipv6 address')
                return

        print(f"{ipv6_validation} is a Valid ipv6 address")
    
    except:
        print(f"An error occurred while validating the IPv6 address")

try:
    with open('ipv6_validation.txt') as f:
        for ipv in f:
            ipv6_validation = ipv.strip()
            is_Valid_hexa(ipv6_validation)

except:
    print("The file 'ipv6_validation.txt' not found")

