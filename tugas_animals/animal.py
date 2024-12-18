class animal:
    #properti
    def __init__(self, nama, makanan, habitat, berkembang_biak):
        self.nama=nama
        self.makanan=makanan
        self.habitat=habitat
        self.berkembsng_biak=berkembang_biak

    #method
    def info_animal(self):
        print('\nNama hewan\t:', self.nama,
              '\nMakanan\t\t:', self.makanan,
              '\nHabitat\t\t:', self.habitat,
              '\nBerkembang biak\t:', self.berkembsng_biak)
        
#objek
# beruang_madu=animal('Beruang Madu', 'Madu', 'hutan', 'Melahirkan')
# beruang_madu.info_animal()