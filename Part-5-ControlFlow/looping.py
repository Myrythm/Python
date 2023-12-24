var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

print("separator".center(30, "-"))

# range
for i in range(10):
    print(i)
print("separator".center(30, "-"))

for i in range(1, 10, 2):
    print(i)
print("separator".center(30, "-"))

#while
counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment
print("separator".center(30, "-"))

# For Nesting
for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)
print("separator".center(30, "-"))

for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1
print("separator".center(30, "-"))

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))
print("separator".center(30, "-"))

# While with break
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")
print("separator".center(30, "-"))

# with list
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)
print("separator".center(30, "-"))

evenNumber = []  # Membuat list kosong untuk menyimpan bilangan genap

for i in range(0, 501, 1):
    if i % 2 == 0:  # Memeriksa apakah bilangan i adalah bilangan genap
        evenNumber.append(i)  # Menambahkan bilangan genap ke dalam list

print(evenNumber)

    