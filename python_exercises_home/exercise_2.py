# Read text file into a variable and replace all newlines with space
# Given: Assume you have a following text file (sample.txt).
# Line1
# line2
# line3
# line4
# line5

# Specify the file path
text = 'sample.txt'

# Read the contents of the file into a variable
with open(text, 'r') as file:
    file_contents = file.read()

# Replace newlines with spaces
file_contents = file_contents.replace('\n', ' ')

# Print the modified contents
print(file_contents)
