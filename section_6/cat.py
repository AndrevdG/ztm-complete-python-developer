# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cats = [
    Cat("Tommy", 8),
    Cat("Jerry", 12),
    Cat("Minous", 4)
]


# 2 Create a function that finds the oldest cat
def find_oldest_cat(list_of_cats):
    oldest_age = 0
    for cat in list_of_cats:
        if cat.age > oldest_age:
            oldest_cat = cat
            oldest_age = cat.age
    return oldest_cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {find_oldest_cat(cats).age} years old.")


# Official solution:
# class Cat:
#     species = 'mammal'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# #Answers:
# # 1 Instantiate the Cat object with 3 cats.
# cat1 = Cat('cat1', 5)
# cat2 = Cat('Cat2', 7)
# cat3 = Cat('Cat3', 3)


# # 2 Create a function that finds the oldest cat.
# def oldest_cat(*args):
#     return max(args)


# # 3 Print out: "The oldest cat is x years old.".
# # x will be the oldest cat age by using the function in #2
# print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
