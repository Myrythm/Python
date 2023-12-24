import numpy as np

var_mat = [[5, 0],
          [1, -2]]

def_mat = [[0 for j in range(2)] for i in range(2)]


for i in range(len(var_mat)):
  for j in range(len(var_mat)):  
    def_mat[i][j] = var_mat[i][j]*2

print(def_mat)

print("")
print("Break".center(20, '-'))
print("")

# With numpy

var_arr = np.array([[5, 0], 
                    [1, -2]])

result = 2 * var_arr
print(result)