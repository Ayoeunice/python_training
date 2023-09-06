# Write all content of a given file into a new file by skipping line number 5
# Specify the input and output file names
input_file_name = 'test.txt'  # Replace with your input file name
output_file_name = 'test1.txt'  # Replace with your output file name

try:
    # Open the input file for reading
    with open('test.txt', 'r') as input_file:
        # Read all lines from the input file into a list
        lines = input_file.readlines()
        # Check if there are at least 5 lines in the file
        if len(lines) >= 5:
            # Remove line 5 (index 4) from the list
            del lines[4]

            # Open the output file for writing
            with open('test1.txt', 'w') as output_file:
                # Write the modified content (without line 5) to the output file
                output_file.writelines(lines)

            print(f"Content from '{input_file}' copied to '{output_file}' with line 5 skipped.")
        else:
            print(f"The input file '{input_file}' does not have at least 5 lines.")
except FileNotFoundError:
    print(f"The input file '{input_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")



