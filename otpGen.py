import random
generateotp=random.randint(000000,100000)
username=input('Username:')
print('Hello..!',username)
print('Here is your OTP for login',generateotp)
password=input('Enter the OTP to login:')
if password ==str(generateotp):
    print('Login Succcess')
else:
    print('incorrect details')