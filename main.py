
integer = 10
floating_point = 20.5
boolean = True
string = "hello world"

print(f"Integer: {integer} \nFloating Point: {floating_point} \nBool: {boolean}\n String: {string}")

my_list = [1, 2, 3, "four", 5.0]

print("List:")
for item in my_list:
    print(item)

my_tuple = (10, 20, 30, "forty", 50.0)

print("Tuple:")
for item in my_tuple:
    print(item)
print("\n")

my_dict = {
    "name": "kshayik",
    "age": 18,
    "is_student": True
}

print("dict:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print()

# func to say hi
def greet(name):
    return f"hi {name}"

# Call the func
print("function:")
print(greet("voidedset"))
print()

print("loops:")
for i in range(5):
    print(i)
print()

# classes :nerd:
class Animal:
    """class for animals"""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} says hello!"

#obj of aanimal
my_animal = Animal("Buddy", "Dog")

print("class and obj")
print(f"Name: {my_animal.name}\nSpecies: {my_animal.species}")
print(my_animal.speak())
