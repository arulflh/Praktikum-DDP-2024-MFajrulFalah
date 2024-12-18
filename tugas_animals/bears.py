from animal import *

class bears(animal):
    def __init__(self, nama, makanan, habitat, berkembang_biak, warna, perilaku):
        super().__init__(nama, makanan, habitat, berkembang_biak)
        self.warna = warna
        self.perilaku = perilaku

    def info_bears(self):
        print('\n### Info Bears ###')
        super().info_animal()
        print('Warna\t\t:', self.warna, '\nPerilaku\t:', self.perilaku)