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

# # Best practise: only import methods/ functions you actually use
# from random import choice

# # show help information for random
# # help(random)

# # show all methods available in package
# # print(dir(random))

# # use a method
# # print(random.choice([1, 2, 3, 4, 5, 6]))
# print(choice([1, 2, 3, 4, 5, 6]))


# working with pip
# in venv: pip install pyjokes
# import pyjokes

# joke = pyjokes.get_joke("en", "chuck")
# print(joke)


# pip commands:
# pip install <lib>
# pip install <lib>==0.4.0  # specific version


# # useful modules
# from collections import Counter, defaultdict, OrderedDict

# # li = [1, 2, 3, 4, 5, 6, 7, 7]
# # sentence = "Blah Blah thinking about python"
# # print(Counter(li))      # count occurences
# # print(Counter(sentence))    # count letters in sentence

# # dictionary = {'a': 1, 'b': 2}
# # print(dictionary['c'])  # throws because the item does not exist

# # with defaultdict you can give a callable function which supplies a default value for missing keys
# # if None a KeyError is thrown
# # callable functions f.i.: list, int, set, str
# # dictionary = defaultdict(lambda: 'no existy', {'a': 1, 'b': 2})
# # print(dictionary['c'])

# # See also: https://www.geeksforgeeks.org/python/ordereddict-in-python/
# # Since python 3.7 normal dicts are also ordered by default, but ordereddict
# # still has function (see above)
# d = OrderedDict()
# d['a'] = 1
# d['b'] = 2

# d2 = OrderedDict()
# d2['b'] = 2
# d2['a'] = 1

# print(d2 == d)

# More useful modules

# import datetime

# print(datetime.time(5, 45, 2))
# print(datetime.date.today())

from array import array

# In Python, array is a collection of items stored at contiguous memory locations.
# The idea is to store multiple items of the same type together.
# Unlike Python lists (can store elements of mixed types),
# arrays must have all elements of same type. Having only homogeneous
# elements makes it memory-efficient.
arr = array('i', [1, 2, 3])
print(arr)
print(arr[0])   # Access array item
