class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i):
        self.i = _i

    def tambah(self, _j):
        return self.i + _j

    def kurang(self, _j):
        return self.i - _j

# Membuat instance dari kelas Kalkulator dengan nilai awal 0
calc = Kalkulator(0)

# Memanggil metode tambah dengan parameter 10
hasil_tambah = calc.tambah(10)
print("Hasil Penambahan:", hasil_tambah)

# Memanggil metode kurang dengan parameter 5
hasil_kurang = calc.kurang(5)
print("Hasil Pengurangan:", hasil_kurang)
