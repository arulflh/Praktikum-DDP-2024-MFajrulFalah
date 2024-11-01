print('Tugas Pertemuan 5')
print()

# list
print('1. Spesifikasi Kendaraan')
list=['MX King', 'Motor Manual', '150 cc', 'Biru, Merah dan Cyan', 'Roda Dua']
list.append('Rp 25.000.000 - Rp 27.000.000')
list.append('Tipe Backbone')
list.insert(2, 'Merk Yamaha')
print(list)
print()

# match
print('2. Luas Bangun Datar')
pilihan = int(input("Masukkan pilihan (1: persegi, 2: lingkaran, 3: segitiga): "))

match pilihan:
    case 1:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas = sisi * sisi
        print("Luas persegi: ", luas)
    case 2:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = 3.14 * jari_jari * jari_jari
        print("Luas lingkaran: ", luas)
    case 3:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print("Luas segitiga: ", luas)
    case _:
        print("Pilihan tidak valid")