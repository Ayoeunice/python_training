# Write all content of a given file into a new file by skipping line number 5
file = open("test.txt", "w")

L = ["line1 \n", "line2 \n", "line3 \n", "line4 \n ", "line5 \n", "line6 \n", "line7 \n"]
file.writelines(L)
file.close()
file = open('test.txt', 'r')
print(file.read())
file.close()



