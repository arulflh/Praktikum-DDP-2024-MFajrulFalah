from animal import *

class fish(animal):
    def __init__(self, nama, makanan, habitat, berkembang_biak, warna, kecepatan):
        super().__init__(nama, makanan, habitat, berkembang_biak)
        self.warna = warna
        self.kecepatan = kecepatan

    def info_fish(self):
        print('\n### Info Fish ###')
        super().info_animal()
        print('Warna\t\t:', self.warna, '\nKecepatan\t:', self.kecepatan)