# Print current time in milliseconds
import time

# Get the current time in seconds since the epoch
current_time_seconds = time.time()

# Convert seconds to milliseconds
current_time_milliseconds = int(current_time_seconds * 1000)

# Print the current time in milliseconds
print("Current Time in Milliseconds:", current_time_milliseconds)
