#Collections are Specialize Data Structures
"""
namedTuple
chainmap
deque
counter
OrderedDict
defaultdict
UserDict
UserList
UserString

"""
#NamedTuple
"""It returns a tuple with a named value for each element in the tuple"""
from collections import namedtuple
a =namedtuple("courses","name","technology")
s=a("data science","python")
print(s)