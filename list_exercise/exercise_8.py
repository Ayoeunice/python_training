# Extend nested list by adding the sublist
# You have given a nested list. Write a program to extend it by
# adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
# Given List:
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
# sub_list = ["h", "i", "j"]
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

# Access the nested sublist where you want to add the sub_list
nested_sublist = list1[2][1][2]

# Extend the nested sublist with the sub_list
nested_sublist.extend(sub_list)

# Print the updated list
print(list1)
