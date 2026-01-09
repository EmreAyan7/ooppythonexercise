class Bakkal:
    def __init__(self, isim,stok=None, kasa=0):
        self.isim = isim
        self.stok = stok if stok is not None else {}
        self.kasa = kasa
    
    def urun_ekle(self, urun_adi, fiyat, miktar):
        if urun_adi in self.stok:
            self.stok[urun_adi]['miktar'] += miktar
            print(f"{miktar} adet {urun_adi} mevcut stoğa eklendi.")
        else:
            self.stok[urun_adi] = {'fiyat': fiyat, 'miktar': miktar}
        print(f"{miktar} adet {urun_adi} eklendi.")
    
    def urun_satin_al(self, urun_adi, miktar):
        if urun_adi not in self.stok:
            print(f"{urun_adi} stokta yok.")
            return
        if self.stok[urun_adi]['miktar'] < miktar:
            print(f"Yetersiz stok: {urun_adi} için sadece {self.stok[urun_adi]['miktar']} adet mevcut.")
            return
        
        toplam_fiyat = self.stok[urun_adi]['fiyat'] * miktar
        self.stok[urun_adi]['miktar'] -= miktar
        self.kasa += toplam_fiyat
        print(f"{miktar} adet {urun_adi} satın alındı. Toplam fiyat: {toplam_fiyat}.")

# Örnek kullanım:
bakkal = Bakkal("Emre Büfe")
bakkal.urun_ekle("sigara", 30, 10)
bakkal.urun_satin_al("sigara", 3)
bakkal.urun_ekle("su", 5, 20)
bakkal.urun_satin_al("su", 2)
bakkal.urun_satin_al("çikolata", 1)  # Stokta olmayan ürün denemesi
bakkal.urun_satin_al("sigara", 20)  # Yetersiz stok denemesi