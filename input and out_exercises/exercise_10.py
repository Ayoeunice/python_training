# Read line number 4 from the following file
f = open("test2.txt", "r")

import linecache

# read fourth line
line = linecache.getline("test2.txt", 4)
print(line)
