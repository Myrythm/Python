class Mobil:
    warna = "Hitam"
    merk = "Toyota"

mobil1 = Mobil()
print(mobil1.warna)

Mobil.warna = "Merah"
mobil2 = Mobil()
print(mobil2.warna)
print("")
# Class Constructor
class Motor:
    def __init__(self):
        self.merk = "Kawasaki"

motor1 = Motor()
motor2 = Motor()

print(motor1.merk)
print(motor2.merk)

motor1.merk = "Honda"
print(motor1.merk)
print(motor2.merk)
print("")

class Car:
   def __init__(self, merk, warna, topSpeed):
       self.merk = merk
       self.warna = warna
       self.topSpeed = topSpeed

Car1 = Car("Toyota Supra", "Black", 200)

print(Car1.merk)
print(Car1.warna)
print(Car1.topSpeed)
print("")