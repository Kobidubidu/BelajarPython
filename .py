def hitung_tarif_parkir(durasi):
    if durasi == 1:
        tarif = 3500
    elif durasi == 2:
        tarif = 5500
    elif durasi == 3:
        tarif = 7500
    else:
        tarif = 7500 + (durasi - 3) * 2000  # Tarif tambahan per jam setelah 3 jam
    return tarif

durasi_parkir = int(input("Masukkan durasi parkir (dalam jam): "))
total_tarif = hitung_tarif_parkir(durasi_parkir)
print(f"Tarif parkir untuk {durasi_parkir} jam adalah {total_tarif} Rupiah.")
