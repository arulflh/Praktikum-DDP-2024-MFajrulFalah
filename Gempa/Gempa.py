class Gempa:
    #func in class=method
    def __init__(self, lokasi, skala):
        self.lokasi=lokasi
        self.skala=skala

    def dampak(self):
        if self.skala<2:
            print('Dampak gempa: tidak berasa')
        elif self.skala>=2 and self.skala <=4:
            print('Dampak gempa: bangunan retak-retak')
        elif self.skala>4 and self.skala <=6:
            print('Dampak gempa: bangunan roboh')
        elif self.skala>6:
            print('Dampak gempa: bangunan roboh dan berpotensi tsunami')

        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'Skala Gempa: {self.skala}')