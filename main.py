from matematika import *
from ruang import *
from datar import *

def menu():
    print("Pilihi program^_^")
    print("1. Operasi aritmatika")
    print("2. Luas bangun datar")
    print("3. Luas permukaan bangun ruang")


    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        aritmatika()
    elif pilihan == 2:
        bangun_datar()
    elif pilihan == 3:
        bangun_ruang()

    

def aritmatika():
    print("pilih operasi aritmatika")
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    print("5. pangkat")
    pilihan = int(input("masukkan pilihan: "))

    if pilihan == 1:
        a = int(input("masukkan angka pertama: "))
        b = int(input("masukkan angka kedua: "))
        print ("hasilnya adalah: ", tambah(a, b))
    elif pilihan == 2:
        a = int(input("masukkan angka pertama: "))
        b = int(input("masukkan angka kedua: "))
        print ("hasilnya adalah: ", kurang(a, b))

    elif pilihan == 3:
        a = int(input("masukkan angka pertama: "))
        b = int(input("masukkan angka kedua: "))
        print ("hasilnya adalah: ", kali(a, b))

    elif pilihan == 4:
        a = int(input("masukkan angka pertama: "))
        b = int(input("masukkan angka kedua: "))
        print( "hasilnya adalah: ", bagi(a, b))
    elif pilihan == 5:
        a = int(input("masukkan angka pertama: "))
        b = int(input("masukkan angka kedua: "))
        print("hasilnya adalah: ", pangkat(a, b))
    else:
        print("pilihan tidak ada")

def bangun_datar():
    print("pilih bangun datar")
    print("1. persegi")
    print("2. segitiga")
    print("3. lingkaran")
    print("4. trapesium")
    print("5. persegi panjang")
    pilihan=int(input("Masukan pilihan: "))

    if pilihan == 1:
        s = int(input("masukkan sisi: "))
        print("luas persegi adalah: ", persegi(s))

    elif pilihan == 2:
        a = int(input("masukkan alas: "))
        t = int(input("masukkan tinggi: "))
        print("luas segitiga adalah: ", segitiga(a, t))

    elif pilihan == 3:
        r = int(input("masukkan jari-jari: "))
        print("luas lingkaran adalah: ", lingkaran(r))
     
    elif pilihan == 4:
        a = int(input("masukkan alas: "))
        b = int(input("masukkan alas: "))
        t = int(input("masukkan tinggi: "))
        print("luas trapesium adalah: ", trapesium(a, b, t))

def bangun_ruang():
    print("pilih bangun ruang")
    print("1. kubus")
    print("2. balok")
    print("3. tabung")
    print("4. kerucut")
    print("5. bola")
    pilihan=int(input("Masukan pilihan: "))
    if pilihan == 1:
        s = int(input("masukkan sisi: "))
        print("luas permukaan kubus adalah: ", kubus(s))
    elif pilihan == 2:
        p = int(input("masukkan panjang: "))
        l = int(input("masukkan lebar: "))
        t = int(input("masukkan tinggi: "))
        print("luas permukaan balok adalah: ", balok(p, l, t))
    elif pilihan == 3:
        r = int(input("masukkan jari-jari: "))
        t = int(input("masukkan tinggi: "))
        print("luas permukaan tabung adalah: ", tabung(r, t))
    elif pilihan == 4:
        r = int(input("masukkan jari-jari: "))
        t = int(input("masukkan tinggi: "))
        print("luas permukaan kerucut adalah: ", kerucut(r, s))
    elif pilihan == 5:
        r = int(input("masukkan jari-jari: "))
        print("luas permukaan bola adalah: ", bola(r))
    else:
        print("pilihan tidak ada")
    


if __name__ == "__main__":
    menu()