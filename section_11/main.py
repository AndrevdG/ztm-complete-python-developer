# # classes or functions from a file in the same folder as the calling file can be imported directly
# import utility
# # when importing classes or functions from a subfolder ('package'), we have to use <folder>.<filename>
# # import shopping.more_shopping.shopping_cart
# # from shopping.more_shopping.shopping_cart import buy
# from shopping.more_shopping import shopping_cart

# print(utility.divide(4, 2))
# # print(shopping.more_shopping.shopping_cart.buy('apples'))
# # print(buy('apples'))
# print(shopping_cart.buy('apples'))

# # check if this file was the original file being run
# if __name__ == "__main__":
#     print('please run this')


# python comes with a lot of built-in modules:
# https://docs.python.org/3/py-modindex.html
# They are installed by default and can be used, though
# they have to be imported

# example import module random
# import random
# import random as r

# Best practise: only import methods/ functions you actually use
from random import choice

# show help information for random
# help(random)

# show all methods available in package
# print(dir(random))

# use a method
# print(random.choice([1, 2, 3, 4, 5, 6]))
print(choice([1, 2, 3, 4, 5, 6]))
