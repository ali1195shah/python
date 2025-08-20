dogs = ["roger", "zoro", 3, True, 4.5, "cat"]

print(dogs)

# the in opperator

print("roger" in dogs)

print(dogs[2])

print("------")

dogs[2] = "BolPancina"

print(dogs)

print(dogs[2:4]) #this is a slice

print(dogs[:3]) 

dogs.append("new dog")
dogs.extend(["Fart"])
dogs += (["Pokemon", "Kutta"])

print(dogs)

print("------")

dogs.remove("zoro")

dogs.pop()

print(dogs)

print("------")

dogs.insert(2, "new Inserted Dog")

dogs[1:1] = ["test1", "test2"]

print(dogs)

print("------")

# sorting

pokemon = ["Blazakin", "Charizard", "Pikachu", "Squirtle", "Bulbasaur", "mew", "Mewtwo", "evee", "snorlax"]

pokemon.sort()

print(pokemon)
 
# pokemon.sort(key = str.lower)
print(pokemon)

# using a global function called sorted


print("------")

sorted(pokemon, key=str.lower)
print(pokemon)