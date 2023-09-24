# Replace each special symbol with # in the following string
# Given:
# str1 = '/*Jon is @developer & musician!!'
import re

str1 = '/*Jon is @developer & musician!!'

# Use regular expression to replace special symbols with '#'
cleaned_str1 = re.sub(r'[^\w\s]', '#', str1)

# print("String with special symbols replaced:", cleaned_str1)
print(cleaned_str1)
