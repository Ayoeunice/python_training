# Check if the first and last number of a list is the same. Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
def are_first_and_last_equal(lst):
    if len(lst) >= 2:
        return lst[0] == lst[-1]
    else:
        # If the list has less than 2 elements, they cannot be the same
        return False

# Example usage:
list1 = [10, 20, 30, 40, 10]
list2 = [75, 65, 35, 75, 30]

result1 = are_first_and_last_equal(list1)
result2 = are_first_and_last_equal(list2)

print(f"Given list1 = [10, 20, 30, 40, 10] Result 1: {result1}")
print(f" list2 = [75, 65, 35, 75, 30] Result 2: {result2}")
