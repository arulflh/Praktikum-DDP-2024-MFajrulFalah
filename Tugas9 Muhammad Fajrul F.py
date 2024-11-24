print('Tugas 9. Muhammad Fajrul F. 0110224072 TI11')
print()

print('1. C to F')
def ctof(celcius):
    konv=(celcius*9/5+32)
    return konv
print(ctof(0))
print(ctof(100))
print()

print('2. Ganjil Genap')
def gg(bilangan):
    rumus=(bilangan%2==0)
    return rumus
print(gg(4))
print(gg(7))
print()

print('3. Kelulusan')
def nilai(keterangan):
    if keterangan>=75:
        print('Lulus.')
    else:
        print('Gagal.')
nilai(80)
nilai(60)
print()

print('4. Bilangan Ganjil')
def bilangan(nilai):
    return[i for i in range(1,nilai,2)]
print(bilangan(20))