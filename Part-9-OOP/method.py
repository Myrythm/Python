def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()


# Object methods
class Motor():
    def __init__(self, merk, topSpeed, color):
        self.merk = merk
        self.topSpeed = topSpeed
        self.color = color

    def tambahKecepatan(self):
        self.topSpeed += 40

motor1 = Motor("Kawasaki", 120, "Green")
print("Kecepatan sebelum: ", motor1.topSpeed)

motor1.tambahKecepatan()
print("Kecepatan sebelum: ", motor1.topSpeed)
print("")

# Static Method
class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

# Class Methods
class Kapal:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_kapal(cls):
        print("Ini adalah metode dari kelas Kapal")
        
Kapal.intro_kapal()
Kapal_1 = Kapal("RawrVant")
Kapal_1.intro_kapal()


