# Python_Assignment
#Arithmetic Exception

try:
  a = 10/0
  print (a)
except ArithmeticError:
 print ("This statement is raising an arithmetic exception.")
else:
 print ("Success.")

# LookUp Error
try:
   a = [1, 2, 3]
   print (a[3]) 
except LookupError:
   print ("Index out of bound error.")

# Attribute Error
class Attributes(object):
    pass

# floating point exception
import math 
print(math.exp(1000))


#exception IndexError
array = [ 0, 1, 2 ]
print (array[3])
