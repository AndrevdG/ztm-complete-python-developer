# Decorators
# for example:
# @classmethod
# @staticmethod


# in python functions are first-class objects, meaning they
# can be assigned to variables, passed as arguments and returned
# from other functions

# def hello():
#     print('Hello!')

# greet = hello
# del hello       # We can delete the original function and the greet variable
#                 # will still point to the function

# print(greet())

# Higher order functions (HOC)

    # A function that accepts another function
    # def greet(func):
    #     func()

    # A function that returns a function
    # def greet2():
    #   def func ():
    #       return 5
    #   return func

# Decorator example

# A decorator is a HOC function that takes a function and
# wraps it in another function:

# def my_decorator(func):
#     def wrap_func():
#         print('*********')
#         func()
#         print('*********')
#     return wrap_func

# @my_decorator
# def hello():
#     print('hello!')

# hello()

# The wrapper function in the decorator allows us to take the
# hello function and enhance it

# How can we make it work with arguments?
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func

@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)

hello("Hello!", ":)")