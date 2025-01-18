import numpy as np
import time
import sys

#  print(np.arange(100)

##a = np.arange(1,10,2) for printing a no in an interval
 ## a = np.linspace(1,5,20) it will create no itream you said in a interval


 ## a = np.arange(12).reshape(3,4)  re shape used to re shape the array
a = np.arange(12).reshape(3,4)
## print(a.ravel()) ravel used to make the array in a row
 ## print(np.std(a))
  # a.dot(b) used for dot product of two matrix
 # b = np.arange(12,24).reshape(3,4)
 ## print(np.hstack((a,b)))
b = a > 4

print(b)

##