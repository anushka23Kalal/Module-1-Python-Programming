import re
print("#Validate Email ,Phone and Age")
email=input("Enter the mail id:")
pattern=r"^[a-zA-Z._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
if re.match(email,pattern):
    print("Email match")
else:

