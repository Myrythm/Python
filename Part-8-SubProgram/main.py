def areaOfRetangle(length, width):
    result = length*width
    return result

count1 = areaOfRetangle(20, 5)
print(count1)
    
count2 = areaOfRetangle(10, 2)
print(count2)

print("Break".center(20, '-'))
print("")

def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))
print("Break".center(20, '-'))
print("")

def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))