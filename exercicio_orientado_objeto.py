class Televisao:
    def __init__(self):    

        self.canal = None 
        self.volume = 0

    def aumentar_volume(self):
        self.volume +=1

    def diminuir_volume(self):
        self.volume -=1

    def alterar_canal(self, canal):
        self.canal = canal

tv = Televisao()
tv.alterar_canal(10)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
tv.alterar_canal(5)

print('Canal:', tv.canal)
print('Volume:', tv.volume)