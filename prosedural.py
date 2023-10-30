def hitung_luas():
    alas = float(input('masukan alas: '))
    tinggi = float(input('masukan tinggi: '))
    print('luas = ', 0.5 * alas * tinggi)

hitung_luas()
hitung_luas()

def x(y):
    if y == 1:
        z = 300
    elif y == 2:
        z = 500
    elif y == 3:
        z = 700
    else:
        z = 700 * (y - 3) * 200
    return z
a = int(input("masukan angka: "))
b = x(a)
print(b)
