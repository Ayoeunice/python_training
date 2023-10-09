# Concatenate two data frames using the following conditions
# Create two data frames using the following two dictionaries.
# GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
# 'Price': [23845, 171995, 135925 , 71400]}
# japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '],
# 'Price': [29995, 23600, 61500 , 58900]}
# Expected Output:
#

import pandas as pd

# Create the two data frames
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '],
                'Price': [29995, 23600, 61500 , 58900]}

# df1 = pd.DataFrame(GermanCars),
# df2 = pd.DataFrame(japaneseCars)
df1 = pd.DataFrame({'Company' : ['Ford', 'Mercedes', 'BMV', 'Audi'],
                    'Price': [23845, 171995, 135925 , 71400]},index=[ 0,1,2,3],)
df2 = pd.DataFrame({'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '],
                'Price': [29995, 23600, 61500 , 58900]},index=[0,1,2,3],)
# Concatenate the data frames vertically (along rows)
# concatenated_df = pd.concat([df1,  df2], ignore_index=True)
frames = [df1, df2]
concatenated_df = pd.concat(frames)
# Print the concatenated data frame
print(concatenated_df)

