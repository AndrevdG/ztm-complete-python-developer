import re

# Regex

# compile a regex object
#   there are also (shortcut) functions that allow patterns without compiling an obj first


# pattern = re.compile('this')
pattern = re.compile(r'([a-zA-Z]).([a])')       # r = raw string, no special characters like \n
string = 'search this inside this text please!'
# print('search' in string)       # simple boolean logic

# a = re.search('this', string)   # <re.Match object; span=(14, 18), match='this'>
a = pattern.search(string)      # search instance
b = pattern.findall(string)     # findall instances
c = pattern.fullmatch(string)   # match whole string
d = pattern.match(string)       # match from beginning of string

# a = re.search('this', string) 
# print(a)
# print(b)
# print(c)
# print(d)

print(a.group(2))
