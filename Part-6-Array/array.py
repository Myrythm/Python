var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)
print("Batas".center(20, "="))

var_arr = [0 for i in range(10)]
print(var_arr)
print("Batas".center(20, "="))

for i in range(10):
    var_arr[i] = i

print(var_arr)
print("Batas".center(20, "="))

# Pemrosesan Sekuensial pada Array
var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i+1
    
    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None
        
    print(f"Current element: {current_element}, next elements: {next_element}")
print("Batas".center(20, "="))

# mencari nilai terbesar dalam array.
var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)
print("Batas".center(20, "="))

# Mencari rata rata array
var_array = [i for i in range(101)]
x = 0
for i in range(len(var_array)):
	x += var_array[i]
result = x/len(var_array)
print(result)