# classes


class Animal:

    def walking(self):
        print("Walking...")
        
class Dog(Animal):

    # This is a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

dog1 = Dog("Roger", 8)

print(dog1.name)
print(dog1.age)
dog1.bark()
dog1.walking() 