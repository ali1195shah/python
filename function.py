def name(name = "Dua"): # function with a dufault parameter Dua
    print("Hello, " + name + "!!!")

name("World")
name("Python")
name("Alice")
name()

def age(name, age):
    print(name + " " + str(age) + "!")

age("Bob", 32)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


# Nested Functions

def outer_Function(phrase):
    def inner_Function(word):
        print(word)

    words = phrase.split(' ')

    for w in words:
        inner_Function(w)

outer_Function("I am going to buy milk today")   

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def counter():
    count = 0

    def increment():
        nonlocal count 
        count += 1
        print(count)
    
    return increment

counter() # this will print out 1

increment = counter() # this will return a function object

print(increment()) 