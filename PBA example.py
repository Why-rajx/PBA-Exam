import re

mobile_no = input("Enter your mobile number: ")

pattern = r'^[6-9]\d{9}$'

if re.match(pattern, mobile_no):
    print("Valid mobile number")
else:
    print("Invalid mobile number")

