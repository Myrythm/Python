class Mobil:
    def __init__(self, merk, color, speed):
        self.merk = merk
        self.color = color
        self.speed = speed

    def tambahKecepatan(self):
        self.speed += 20

class Sport(Mobil):
    def turbo(self):
        self.speed += 40

    def tambahKecepatan(self):
        super().tambahKecepatan()
        print("Hati Hati")

mobil1 = Sport("Toyota", "Yellow", 160)
mobil1.tambahKecepatan()
print(mobil1.speed)
print("Turbo:")
mobil1.turbo()
print(mobil1.speed)
