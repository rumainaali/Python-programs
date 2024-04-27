import sys
email=input('Enter your email:')
if len(email)<10:
  print('Invalid email id, length must be minimum 10')
  sys.exit()
  
if '@' not in email or '.' not in email:
    print('Invalid email id,')
    sys.exit()

if email.count('@')>1:
    print('Invalid email id, email must contain only one @ symbol')
    sys.exit()
    
split_string=email.split('@')
print(split_string)