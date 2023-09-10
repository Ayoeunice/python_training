# Use a loop to display elements from a given list present at odd index positions
# Given:
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

given_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#print("Elements at odd index positions:")
for i in range(1, len(given_list), 2):
    print(given_list[i])
