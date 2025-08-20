# sets


set1 = {"Roger", "Whitebeard", "Blackbeard", "Kaido", "Roger", "Kaido"}
set2 = {"Big Mom", "Shanks", "Luffy", "Kaido"}

intersect = set1 & set2 # check what is common in both sets

print(intersect)

union = set1 | set2 # combine both sets and removes dups
print(union)

difference = set1 - set2 # what is in set1 but not in set2
print(difference)

print(set1 > set2) # check if set1 is a superset of set2

print(list(set1)) # converts set to a list with no dups