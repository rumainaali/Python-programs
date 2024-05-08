'''Date:8/05/2024
IPV4 - IP Address Validation
Example:123.213.165.0
'''
import sys

ip=input('Enter the IP Address:')
octets = ip.split('.')
if len(octets)!=4:
    print('Number of octets must be ')
    sys.exit()
    
for octet in octets:
    if not octet.isdigit():
        print('Octet must be only digits')
        sys.exit()
    
    int_octet=int(octet)
    if int_octet>=0 and int_octet<=255:
        continue
    print('Invalid must contain from 0 to 255')
    sys.exit()
print('Valid IP Address')
    

    
    
