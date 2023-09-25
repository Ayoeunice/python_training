# Slice list into 3 equal chunks and reverse each chunk
# Given:
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# Calculate the length of the list
list_length = len(sample_list)

# Calculate the size of each chunk (assuming 3 equal chunks)
chunk_size = list_length // 3

# Slice the list into 3 equal chunks
chunks = [sample_list[i:i+chunk_size] for i in range(0, list_length, chunk_size)]

# Reverse each chunk
reversed_chunks = [chunk[::-1] for chunk in chunks]

# Print the reversed chunks
for i, chunk in enumerate(reversed_chunks):
    print(f"Chunk {i+1}:", chunk)
