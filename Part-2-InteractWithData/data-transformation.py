# Uppercase letters
kata = 'azure'
kata = kata.upper()
print(kata)

# lowercase letters
kata = 'MAMANK'
kata = kata.lower()
print(kata)

# rstrip characters
print("Rawr          ".rstrip())

# lstrip characters
print("           Rawr".lstrip())

# strip characters
print("         Rawr          ".strip())
kata = 'CodeCodeHuntCodeCode'
print(kata.strip("Code"))

# start with
print('Jaya Esports'.startswith('Jaya'))

# endswith()
print('Jaya Esports'.endswith('Esport'))

# join strings
print(' '.join(['Rawr','Esports', '!']))
print('123'.join(['Rawr','Esports']))

# split strings
print('Dicoding Indonesia !'.split())

print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))

# replace strings
string = "Ayo Gabung Divisi Valorant di Rawr Esports"
print(string.replace("Valorant", "Dota 2"))

#  Check string UPPER
kata = 'MAMANG'
print(kata.isupper())

#  Check string lowercase
kata = 'mamang'
print(kata.islower())

# Check string alpha
kata = 'rawr'
print(kata.isalpha())

# isalnum()
kata = 'dicoding123'
print(kata.isalnum())

# isdecimal()
print('123'.isdecimal())

# isspace()
print('         '.isspace())

# istitle()
print('Rawr Esports'.istitle())

# Formatting  strings
# zfill()

teks = 'Code'
tambah_number = teks.zfill(5)
print(tambah_number)

# rjust()
print('Rawr'.rjust(20))

# ljust()
print('Rawr'.ljust(20, ''))

# center()
print('Rawr'.center(20, '-'))

# String literals
st1 = "Jum'at"
st1 = 'ma\'ap'
print(st1)

print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")

# raw string
print(r'Rawr\Esport')

