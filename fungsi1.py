#praktek1
def x(y):
    if y == 1:
        z = 300
    elif y == 2:
        z = 500
    elif y == 3:
        z = 700
    else:
        z = 700 + (y - 3) * 200
    return z
a = int(input())
c = x(a)
print(c)

#praktek2
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
#pemanggilan fungsi
print("luas Persegi : %d" % luas_persegi(6))

def luas_persegi_panjang(panjang,lebar):
    l = panjang * lebar
    return l

print ("luas persegi panjang : %d" % luas_persegi_panjang(9,5))

#praktek3
#membuat variabel global
nama = "python"
versi = "1.0.0."

def help():
    nama = "c#"
    versi = '1.0.2'
    #mengakses variabel lokal
    print("Nama: %s" % nama)
    print("versi: %s" % versi)

#mengakses variabel global
print("nama: %s" % nama)
print("versi: %s" % versi)

#memanggil fungsi help()
help()