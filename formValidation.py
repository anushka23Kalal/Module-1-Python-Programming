import re
print("#Validate Email#")
email = input("Enter the mail id:")
pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    print("Email valid")
else:
    print("Email invalid")

print("#Validate Phone#")
phone = input("Enter the Phone Number:")
pattern2 = r"^[6-9]\d{9}$"
if re.match(pattern2, phone):
    print("Phone number is valid")
else:
    print("Phone number is invalid")

print("#Age Validation#")
age = input("Enter the age:")
pattern3 = r"^\d{1,3}$"
if re.match(pattern3, age):
    print("Age Valid")
else:
    print("Age Invalid")
