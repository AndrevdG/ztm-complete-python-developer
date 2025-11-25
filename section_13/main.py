# # File IO
# my_file = open("input.txt")
# # print(my_file.read())

# # # empty: after reading the file before, the cursor is now at the
# # # end of the file
# # print(my_file.read())

# # # we can move the cursor back to the beginning (index 0)
# # my_file.seek(0)
# # print(my_file.read())

# # we can also read lines
# # print(my_file.readline())
# # print(my_file.readline())

# # We can use readlines to get a list containing the lines
# print(my_file.readlines())

# # when you are done you should close the file
# my_file.close()

# when using with the file is automatically closed at the end of the codeblock
# with open("input.txt") as my_file:
#     print(my_file.readlines())

# using mode we can open the file for:
# r - read: open file for reading, cursor at beginning of file
# w - write: open file if it exists or create new file. OVERWRITES
# r+ - readwrite: open file for reading and writing. cursor at 0. Fails if not exists
# a - append: open file for append only, created file if not exists
# for more modes: https://www.geeksforgeeks.org/python/file-mode-in-python/
# with open("input.txt", mode="r+") as my_file:
#     text = my_file.write('Hey, it\'s me')
#     print(text)

# When using file paths on programs that may run on different architectures
# you can use the pathlib module which helps dealing with paths in different os types

# commonly we will use except blocks when working with files
try:
    with open("input2.txt", mode="r") as my_file:
        print(my_file.read())
except FileExistsError as err:
    print("file does not exist")
    raise err
