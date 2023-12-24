# Primitive Data Types
x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))


var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

# Boolean variables
x = True
print(type(x))

x = False
print(type(x))

# String variables
x = 'Anjay'
print("X bertipe: ", type(x))

# Multiline variables
multi_line = """Halo!
Kapan Mau Jalan?
Kapan-Kapan."""

print(multi_line)


# formatted String variables
name = "Mr X"
print(f"Hello, nama saya {name}")

# Formating  %
ame = "Mr Y"
print("Nama saya %s" % (name))

# Str Format
name = "Mr Z"
print("Nama saya {}".format(name))
