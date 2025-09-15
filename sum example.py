#summation
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])

newarr = np.sum([arr1,arr2])

print(newarr)

#Summation axis 1
import numpy as np

arr1 = np.array([1,2,4])
arr2 = np.array([1,2,3])

newarr = np.sum([arr1,arr2],axis = 1)

print(newarr)

#Cummulative Sum
import numpy as np

arr = np.array([1,2,3])

newarr = np.cumsum(arr)

print(newarr)