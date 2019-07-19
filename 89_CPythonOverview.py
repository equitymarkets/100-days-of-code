#Day 89: Exploring CPython as it relates to the internals of the
#Python programming language 
#

import Fib



x = Fib.Fib_Func()
 
y = 10 

input()
print("  ")
print(dir(x))                           #all possible operations on object
print("  ")
print(dir(y))
print("  ")
input()
print(type(x))                          #type of object
print("  ")
print(type(y))
print("  ")
input()
print(id(x))                            #unique(random) ID number
print("  ")
print(id(y))
print("  ")
input()
print(map(sum(x), x))                   #map to memory location
print("  ")
print(oct(y))                           #octal(base 8) representation
print("  ")                             #0o12 = 10 
