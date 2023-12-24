# matrix with numpy is more efficient

import numpy 
import sys

var_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_numpy = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("The overall size of the list element in bytes = ",sys.getsizeof(var_list)*len(var_list))
print("The overall size of the NumPy element in bytes = ", var_numpy.size*var_numpy.itemsize)
