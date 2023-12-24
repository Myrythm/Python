import numpy

matriks = numpy.array( [[1, 0, 1, 0, 1],
                        [0, 1, 0, 1, 0],
                        [1, 0, 1, 0, 1]])
     
print(matriks)

print("")
print("Break".center(20, "="))
print("")

matrix = numpy.array([[0 for i in range(4)] for j in range(3)])
print(matrix)

var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14,	 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
           
print(var_mat[2][1])