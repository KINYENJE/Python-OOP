# define a class dog
class Dog:
    #class attribute
    species = 'mammal'


    # Instance attribute
    # Use the __init__() method to initialize an object’s initial attributes by giving them their default value (or state).
    # This method must have at least one argument as well as the self variable, which refers to the object itself (e.g., Dog).
    def __init__(self, name, age):
        self.name = name
        self.age = age


    # Instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)




# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
bosco = Dog('Bosco',7)

# Accessing the instance attribute
print('{} is {} and {} is {}.'.format(philo.name, philo.age, bosco.name, bosco.age))

# Accessing the instance methods
print(bosco.description())
print(bosco.speak('woof woof'))



# is Bosco a mammal
if bosco.species == 'mammal':
    print("{0} is a {1}!".format(bosco.name, bosco.species))





#   Determinre the oldest dog
def get_biggest_number(*args):
    return max(args)

print("The oldest dog is {} years old.".format(get_biggest_number(bosco.age, philo.age, mikey.age)))

