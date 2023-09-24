# Remove empty strings from a list of strings
# Given:
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# Remove empty strings (including "", None) using a list comprehension
filtered_str_list = [s for s in str_list if s is not None and s != ""]

print("List after removing empty strings:", filtered_str_list)
