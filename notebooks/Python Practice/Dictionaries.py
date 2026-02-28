# creating a dictionary
captains = dict() # or just say captian = {}

# adding items to a dictionary one by one
captains['enterprise'] = 'Picard'
captains['voyager'] = 'Janeway'
captains['defiant'] = 'Sisko'

# printing the dictionary
print(captains)

# printing a specific item
print(captains['enterprise'])

# if statement: check for keys named 'enterprise' and 'discovery', if the key does not exist, set their values to 'unknown'
if 'enterprise' not in captains:
    captains['enterprise'] = 'unknown'
if 'discovery' not in captains:
    captains['discovery'] = 'unknown'

# print the dictionary again
print(captains)

# print the keys
print(captains.keys())

# for loops- iterating over dictionaries
# write a for loop that prints each key and value in the dictionary
for key, value in captains.items():
    print(f"The {key} is captained by {value}")

