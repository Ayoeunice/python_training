# Checks if one set is a subset or superset of another set. If found, delete all elements from that set
# Given:
# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

# Check if first_set is a subset of second_set
is_first_subset_second = first_set.issubset(second_set)

# Check if second_set is a subset of first_set
is_second_subset_first = second_set.issubset(first_set)

# Check if first_set is a superset of second_set
is_first_superset_second = first_set.issuperset(second_set)

# Check if second_set is a superset of first_set
is_second_superset_first = second_set.issuperset(first_set)

# If first_set is a subset of second_set, clear it
if is_first_subset_second:
    first_set.clear()

# If second_set is a superset of first_set, clear it
if is_second_superset_first:
    second_set.clear()

# Print the results
print("First set is subset of second set -", is_first_subset_second)
print("Second set is subset of First set -", is_second_subset_first)
print("First set is Super set of second set -", is_first_superset_second)
print("Second set is Super set of First set -", is_second_superset_first)
print("First Set", first_set)
print("Second Set", second_set)

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

# Check if first_set is a subset of second_set
if first_set.issubset(second_set):
    # If it's a subset, remove all elements from first_set
    first_set.clear()
elif first_set.issuperset(second_set):
    # Check if first_set is a superset of second_set
    # If it's a superset, remove all elements from second_set
    second_set.clear()

# Print the updated sets
print("Updated first_set:", first_set)
print("Updated second_set:", second_set)

