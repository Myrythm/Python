# List
# List merupakan jenis kumpulan data terurut (ordered sequence) dan salah
# satu tipe data yang sering digunakan pada Python. 
x = [1, 2.2, 'Jaya Esports']
print(type(x))

# mutable list
x = [1, 2.2, 'Jaya Esports']
x[0] = 'Indonesia'
print(x)

# indexing
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])

# Slicing
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

# Tuple
# Tuple adalah jenis dari list yang tidak dapat diubah elemennya. Umumnya, tuple digunakan untuk 
# data yang bersifat sekali deklarasi dan dapat dieksekusi lebih cepat.

x = (1, "Dicoding", 1+3j)
print(type(x))

x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])

# Set
# Set adalah kumpulan item bersifat unik, tanpa urutan (unordered collection), dan 
# dapat diinisialisasikan dengan kurawal “{}” di mana setiap elemennya dipisahkan dengan koma.

x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

interselcetion = set1.intersection(set2)
print("Interselection:", interselcetion)

# dictionary 
# Dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan. 
# Dictionary dapat digunakan untuk menyimpan data kecil hingga besar. Pada Python, 
# dictionary didefinisikan dengan kurawal dan tambahan definisi berikut.

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

print(type(x))
print(x ['name'])
# tambah dict
x ['Job'] = "Web Developer"
print(x)
# hapus dict
del x['isMarried']
print(x)
# ubah dict
x ['name'] = "Azka"
print(x)


print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))


# print conversion  DICTIONARY
print(dict([[1,2],[3,4]]))
print(dict([(3,26),(4,44)]))