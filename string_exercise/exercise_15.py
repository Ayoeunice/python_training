# Remove special symbols / punctuation from a string
# Given:
# str1 = "/*Jon is @developer & musician"
import re

str1 = "/*Jon is @developer & musician"

# Use regular expression to remove special symbols and punctuation
cleaned_str1 = re.sub(r'[^\w\s]', '', str1)

# print("String with special symbols removed:", cleaned_str1)
print(cleaned_str1)
