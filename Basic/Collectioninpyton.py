#Collections are Specialize Data Structures

# namedTuple
# chainmap
# deque
# counter
# OrderedDict
# defaultdict
# UserDict
# UserList
# UserString

#NamedTuple
#It returns a tuple with a named value for each element in the tuple
from collections import namedtuple
a =namedtuple("courses","name , technology")
s=a("data science","python")
print(s)
s=a._make(["data science","python"])
print(s)
#Deque
#Deque pronunced as deck is an optimised list to perform insertion and deletion easily
from collections import deque
a=['s','u','b','a','s','h']
d=deque(a)
print(d)
d.append('devil')
print(d)
d.pop()
print(d)
#Chainmap
#Chainmap is a dictionary like class for creating a single view of multiple mappings.
from collections import ChainMap
a={1:'eureka',2:'python'}
b={2:'ruby',3:'java'}
a1=ChainMap(a,b)
print(a1)
#Counter
#Counter is a dictionary subclass for counting hashable objects..
from collections import Counter
a=[1,1,1,2,3,2,2,4,5,4,5,4,3,6,2,2]
c=Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
#Subtract 2 one times and 6 1 times
sub={2:1,6:1}
print(c.subtract(sub))
print(c.most_common())
#OrderedDict
#OrderedDict is dictionary subclass which remembers the order in which the entries were done
from collections import OrderedDict
d=OrderedDict()
d[1]='e'
d[2]='d'
d[3]='u'
d[4]='r'
d[5]='e'
d[6]='k'
d[7]='a'
print(d)
d[1]='p'
print(d.keys())
print(d)
#Defaultdict
#Defaultdict is a dictionary subclass which calls a factory function to supply missing values
from collections import defaultdict
d=defaultdict(int)
d[1]='python'
d[2]='edureka'
print(d[3])
#it will not show you any error
# a={1:'python',2:'edureka'}
# print(d[3])
#UserDict,UserList,UserString
#UserDict is a wrapper around dictionary objects for easier dictionary objects for easier dictionary sub-classing
#UserList is a wrapper around list objects for easier List sub-classing
#UserString is a wrapper around string objects for easier string sub-classing