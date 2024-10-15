'''create_password =input("create a password:")
if len(create_password) < 8:
  print ("password must be 8 characters")
elif  create_password.isalnum():
    print("password must be alphanumeric")
else:
    print("password created")'''
   
'''password = 'john'
print(password.isalnum()) 
print(not password.isalnum()) '''

create_password = input("Create a password:")

if len(create_password) < 8:
    print("Password must be at least 8 characters.")
elif create_password.isalnum():
    print("Password must contain special characters.")
elif create_password.isalpha():
    print("Password must contain numbers.")
elif create_password.isdigit():
    print("Password must contain letters.")
else:
    print("Password created!")

