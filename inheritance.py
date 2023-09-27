# class Dog:
#     def __init__(self, breed):
#         self.breed = breed
#
# spencer = Dog("German Shepherd")
# print(spencer.breed)

#parent class
class Dog:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def description(self):
        return "{} is {} years old".format(self.name, self.age)


    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {} ".format(self.name, speed)


class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child classes inherit attributes and
# behaviours from the parent class
tim = Bulldog('Tim', 12)
print(tim.description())
print(tim.run("slowly"))

# Is Tim an instance of dog()?
print(isinstance(tim, Dog))   # True
print(isinstance(tim, Bulldog))  # True
print(isinstance(tim, RussellTerrier))   # False
