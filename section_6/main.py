# OOP

# 4 Pillars of OOP
# - Encapsulation: Bundles data (attributes) and methods (functions) that operate on the data into a single unit, or
#       class, and restricts direct access to some of the object's components
# - Abstraction: Hides complex implementation details and shows only the essential features of an object to the user
# - Inheritance: Allows a new class (child class) to inherit properties and methods from an existing class
#       (parent class). This promotes code reuse
# - Polymorphism: Means "many forms" and allows objects of different classes to be treated as objects of a common
#       superclass. It allows a single method to have different implementations depending on the object
#       it's called on.

# class BigObject:
#     pass

# Private or Public
# Python has no real privacy, any function or variable in a class can be overwritten
# Best practise is to name private variables or functions starting with a _ to show it should not be altered
# However, nothing prevents you from doing so
# Example, _name would be marked as 'should be' private:
# class PlayerCharacter:
#     def __init__(self):
#         self._name

# Dunder methods
# python classes can have loads of methods with double underscores, like __init__
# These are methods built-in to Python and normally we should not create our own
# dunder methods.


# obj1 = BigObject()

# print(type(obj1))

# class PlayerCharacter:
#     membership = True       # class object attribute - Static value across instances

#     def __init__(self, name, age):  # init/constructor method
#         if self.membership:         # can also use PlayerCharacter.membership because it is a class object attribute
#             self.name = name    # attribute
#             self.age = age

#     def run(self):
#         print('run')

#     def shout(self):
#         print(f"My name is {self.name}")

#     @classmethod
#     def adding_things(cls, num1, num2):  # Class methods can be called even when the class is not instantiated
#         # return num1 + num2
#         return cls('Teddy', num1 + num2)    # a class method can instantiate the class

#     @staticmethod
#     def adding_things2(num1, num2):  # Class methods can be called even when the class is not instantiated
#         return num1 + num2               # a static method does not have access to the class


# # player1 = PlayerCharacter('Jack', 33)
# # print(player1.name)
# # print(player1.age)
# # player1.run()
# # player1.membership = False

# # print(player1.membership)

# print(PlayerCharacter.adding_things(2, 3))


# Example(s)

# class User():
#     def sign_in(self):
#         print('logged in')

#     def attack(self):
#         print('do nothing')


# class Wizard(User):         # inheritance
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):           # redefines the method inherited from User()
#         User.attack(self)       # can call the orginal method from the parent class (polymorphism)
#         print(f'attacking with power of {self.power}')


# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with arrows: arrows left {self.num_arrows}')

# def player_attack(char):
#     char.attack()

# wizard1 = Wizard("Merlin", 50)
# archer1 = Archer("Robin", 100)

# wizard1.attack()
# archer1.attack()

# print(isinstance(wizard1, object))

# player_attack(wizard1)      # polymorphism example
# player_attack(archer1)

# class User():
#     def __init__(self, email):
#         self.email = email

#     def sign_in(self):
#         print('logged in')


# class Wizard(User):
#     def __init__(self, name, power, email):
#         super().__init__(email)
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f'attacking with power of {self.power}')


# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with arrows: arrows left {self.num_arrows}')

# def player_attack(char):
#     char.attack()

# wizard1 = Wizard('Merlin', 50, 'wizard1@localhost')
# print(wizard1.email)

# # introspection - determine the type of an object at runtime
# print(dir(wizard1))     # show all of the methods and attributes of wizard1

# dunder methods
# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age


# action_figure = Toy('red', 0)
# print(action_figure.__str__())  # dunder methods are special methods that allow us to use
# print(str(action_figure))       # python builtin functions
#                                 # https://docs.python.org/3/reference/datamodel.html#special-method-names


# # changing dundermethods. We can update dundermethods in our class if we r
# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#         self.my_dict = {
#             'name': 'Yoyo',
#             'pets': False
#         }

#     def __str__(self):
#         return f'{self.color}'
    
#     def __len__(self):
#         return 5
    
#     def __call__(self):
#         print('yes?')

#     def __getitem__(self, i):
#         return self.my_dict[i]
        


# action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str(action_figure))
# print(len(action_figure))
# print(action_figure['name'])

# Multiple inheritance  -> creates a lot of additional complexity
#   Be cautious when using this

class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f'arrows remaining {self.num_arrows}')

    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)

hybrid_borg1 = HybridBorg('locutus', 50, 100)
hybrid_borg1.run()
hybrid_borg1.check_arrows()


# Method resolution order
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num)
print(D.mro())

# https://medium.com/@ruitcatarino/understanding-pythons-method-resolution-order-mro-f7cbcec36993
# When multiple inheritance gets bigger and deeper, the resolution also gets more complex
# (I struggle to follow the bigger examples atm...)