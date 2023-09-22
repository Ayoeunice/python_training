# Write all content of a given file into a new file by skipping line number 5
# Create a test.txt file and add the below content to it.
# Given test.txt file:

# line1
# line2
# line3
# line4
# line5
# line6
# line7
# Expected Output: new_file.txt
# line1
# line2
# line3
# line4
# line6
# line7

# Open the original file for reading
#with open('test.txt', 'r') as original_file:
    # Create a new file for writing
   # with open('test.txt', 'w') as new_file:
        # Initialize a line counter
        #line_count = 0

        # Iterate over each line in the original file
        #for line in original_file:
            # Increment the line counter
            #line_count += 1

            # Skip line number 5
            #if line_count != 5:
                # Write the line to the new file
                #new_file.write(line)


# Open the original file for reading
with open('test.txt', 'r') as original_file:
    # Read all the lines from the original file
    lines = original_file.readlines()

# Create a new file for writing
with open('new_file.txt', 'w') as new_file:
    # Write all lines except the 5th line (index 4)
    for i, line in enumerate(lines):
        if i != 4:
            new_file.write(line)

# Print a message to indicate the process is completed
print("Content copied to new_file.txt with line 5 skipped.")
print(new_file)
