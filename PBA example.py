"""import re 
mobile_no = (input("enter your mobile no : "))

pattern = r'^[6-9] \ d{9} $'
if re.match(pattern,mobile_no):
    print("valide mobile no :")
else:
    print("invalid mobile no :")"""

import re

mobile_no = input("enter your mobile no : ")


pattern = r'^[6-9]\d{9}$'
if re.match(pattern, mobile_no):
    print("valid mobile no :")
else:
    print("invalid mobile no :")
