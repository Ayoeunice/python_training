# Check file is empty or not
import os

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

file_path = 'test.py'

if is_file_empty(file_path):
    print(f'The file {file_path} is empty.')
else:
    print(f'The file {file_path} is not empty.')
