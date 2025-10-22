# is_old = True
# is_licensed = True

# # If / elif / else
# if is_old and is_licensed:
#     print("go baby!")
# else:
#     print("no no!!")

# Thruthy and Falsy:
# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

# # Ternary operator
# can_drive = "driving allowed" if is_old and is_licensed else "driving not allowed"
# print(can_drive)

# Short circuiting
# When determing the result of a condition, the interpreter
# will stop processing the condition when the outcome is sure
# False and True : Interpreter stops after false because the outcome is already known

# is_Friend = True
# is_User = True
# if is_Friend or is_User:        # if is_Friend is True, the stuff after 'or' is skipped
#     print("Friendsies!")

# is_magician = False
# is_expert = True

# if is_magician and is_expert:
#     print("you are a master magician")
# elif is_magician:
#     print("at least you are getting there")
# else:
#     print("you need magic powers")

# for item in 'Zero to Mastery':
#     print(item)

# iterable - list, dictionary, tuple, set, string

# user = {
#     'name': 'Golem',
#     'age': 5006,
#     'can_swim': False
# }

# for item in user.items():
#     print(item)

# for item in user.values():
#     print(item)

# for item in user.keys():        # just 'user' would do the same but this is more descriptive
#     print(item)

# for k, v in user.items():
#     print(k, v)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total = 0
# for item in my_list:
#     total += item
# print(f"Sum is equal to {total}")

# range is (?) a special type of object that you can iterate over
# range(100) -> shortcut for range(0,100) 0 till 100 (99 being the last number)
# range(0, 100, 2) -> adding a step of 2 (0, 2, 4, 6, etc)
# range(10, 0, -1)  -> step backwards
# list(range(10)) -> create a list of 10 integers [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for _ in range(0, 10):          # when we don't need number value of each loop common practise is to
#     print('x')                  # use _ to show we have no interest in the value (though we could still use '_')

# for i, char in enumerate('hello'):  # enumerate gives us the index and value for an iterable
#     print(i, char)

# i = 0
# while i < 50:
#     print(i)
#     i += 1
# else:                               # You can use an else after a while, unless there is a break
#     print('done with looping')

# break         Break out of the loop
# continue      Continue with next iteration without doing the rest of the loop
# pass          Passes to the next line (...), used as placeholder sometimes

# # Exercise!
# # Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. 
# This will reveal an image!
# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
# ]

# for row in picture:
#     for column in row:
#         if column == 0:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print('')

# # Excercise: Check for duplicates
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = []
# for item in some_list:
#     if some_list.count(item) > 1 and item not in duplicates:
#         duplicates.append(item)
# print(duplicates)

# Functions

# # function with parameters
# def hello(name, emoji):
#     print(f"hello {name} {emoji}")


# # positional arguments
# hello("André", "😘")

# # keyword (best practise is to keep the order the same as in the function definition)
# hello(emoji="😘", name="Karel")

# # A function without return will always return 'None'
# def my_sum(num1, num2):
#     return num1+num2

# # Functions should do one thing
# # Functions should return something


# print(my_sum(5, 6))

# # Docstrings
# def something(a):
#     '''
#     Info: this function does basically nothing
#     '''
#     print(a)


# # hover over the function to show the docstring
# something('!!')

# # print help
# help(something)
# print(something.__doc__)


# # *args and **kwargs
# def super_func(*args, **kwargs):      # allows any number of arguments, kwargs
#     total = 0
#     for items in kwargs.values():       # kwargs is a dictionary with all keywords + values
#         total += items
#     return sum(args) + total        # args actually is a tupel with all arguments


# # Important Rule: params, *args, default parameters, **kwargs

# print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))


# def highest_even(li):
#     li.sort(reverse=True)
#     for item in li:
#         if item % 2 == 0:
#             return item


# print(highest_even([10, 2, 3, 4, 8, 11]))

# # Walrus operator

# a = 'helloo!!!!!!!!!!'
# if ((b := len(a)) > 10):
#     print(f'too long, {b} elements')

# while (n := len(a)) > 1:
#     print(n)
#     a = a[:-1]

# Scope - What variables do I have acces to?
# - global
# - function scope

# Rules:
# 1 - start with local
# 2 - parent local
# 3 - global (no indentation)
# 4 - built-in python function

# global // nonlocal can be used to reference a variable from global/parent scope

