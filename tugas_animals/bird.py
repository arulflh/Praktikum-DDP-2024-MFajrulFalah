from animal import *

class bird(animal):
    def __init__(self, nama, makanan, habitat, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, habitat, berkembang_biak)
        self.warna = warna
        self.paruh = paruh

    def info_bird(self):
        print('\n### Info Bird ###')
        super().info_animal()
        print('Warna\t\t:', self.warna, '\nParuh\t\t:', self.paruh)

# bird=bird('Elang', 'Daging', 'Tebing dan pohon', 'Bertelur', 'Coklat', 'Tajam melengkung')
# print('\n### Info Bird ###')
# bird.info_bird()