# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
# Note you must adhere to the following conditions:
# The lottery number must be 10 digits long.
# All 100 ticket number must be unique.


import random

# Generate a list of 100 unique random lottery tickets
lottery_tickets = set()

while len(lottery_tickets) < 100:
    ticket = str(random.randint(1000000000, 9999999999))
    lottery_tickets.add(ticket)

# Convert the set to a list
lottery_tickets = list(lottery_tickets)

# Pick two lucky tickets as winners
winners = random.sample(lottery_tickets, 2)

# Print the list of all lottery tickets
print("All lottery tickets:")
for ticket in lottery_tickets:
    print(ticket)

# Print the two lucky winners
print("\nLucky winners:")
for winner in winners:
    print(winner)
