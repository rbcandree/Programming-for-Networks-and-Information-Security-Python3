# 4 Given a time in the format: hh:mm:ss, use regular expressions to programmatically
# validate that the given time matches the format. 
# A successful match should have two digits in each the hours, minutes and seconds.

# Expected output:
# Time to validate: 11:50:22
# Is valid: True
# Time to validate: 11:65:78
# Is valid: False

import re

def time_validate(user_input):
    print(f"Time to validate: {user_input}")
    pattern = r'^[0-2][0-4]+:[0-5][0-9]+:[0-5][0-9]$'   # '00-24:00-59:00-59'
    match = re.search(pattern, user_input)
    if match:
        return True
    else:
        return False

did_it_match = time_validate(input("Time data in the format <hh:mm:ss>: " ))
print("Is valid:", did_it_match)