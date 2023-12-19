# Let’s write a program to validate an e-mail address.
# We can use re.fullmatch(pattern, string) method here. 
# fullmatch() returns match object if the whole string matches the pattern, otherwise it returns None.

import re
pattern = r'[a-zA-Z0-9_.]+@gmail.com'
email_to_check = input("Please, enter your email:")
validation = re.fullmatch(pattern, email_to_check)
print(validation)