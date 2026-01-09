class Kitap:
    def __init__(self, ad, yazar,ödünce_alindi_mi=False):
        self.ad = ad
        self.yazar = yazar
        self.ödünce_alindi_mi = ödünce_alindi_mi

        
    def kitap_bilgisi(self):
        return f"Kitap Adı: {self.ad}, Yazar: {self.yazar}, Ödünç Alındı Mı: {self.ödünce_alindi_mi}"
    
class Üye:
    def __init__(self,isim, ):
        self.isim = isim
        self.__ödünç_alınan_kitaplar = []
    

    def ödünç_al(self,kitap):
        if not kitap.ödünce_alindi_mi:
            kitap.ödünce_alindi_mi = True
            self.__ödünç_alınan_kitaplar.append(kitap)
            return f"{self.isim} adlı üye '{kitap.ad}' kitabını ödünç aldı."
        return f"'{kitap.ad}' kitabı zaten ödünç alınmış."
    
    def __ödünç_alınan_kitapları_göster(self):
        if not self.__ödünç_alınan_kitaplar:
            return "Ödünç alınan kitap yok."
        kitap_listesi = ", ".join([kitap.ad for kitap in self.__ödünç_alınan_kitaplar])
        return f"Ödünç alınan kitaplar: {kitap_listesi}"
    
class Kütüphane:
     def __init__(self):
         self.__kitaplar = []
         self.__üyeler = []
        
     def kitap_ekle(self,kitap):
            self.__kitaplar.append(kitap)
            return f"'{kitap.ad}' kitabı kütüphaneye eklendi."
     
        def üye_ekle(self,üye):
            self.__üyeler.append(üye)
            return f"'{üye.isim}' adlı üye kütüphaneye eklendi."
     
        def __kitapları_göster(self):
            if not self.__kitaplar:
                return "Kütüphanede kitap yok."
            kitap_listesi = ", ".join([kitap.ad for kitap in self.__kitaplar])
            return f"Kütüphanedeki kitaplar: {kitap_listesi}"
     
        def __üyeleri_göster(self):
            if not self.__üyeler:
                return "Kütüphanede üye yok."
            üye_listesi = ", ".join([üye.isim for üye in self.__üyeler])
            return f"Kütüphanedeki üyeler: {üye_listesi}"
     

kütüphane = Kütüphane()
kitap1 = Kitap("1984", "George Orwell")
kitap2 = Kitap("Suç ve Ceza", "Fyodor Dostoevski")
üye1 = Üye("Ahmet")
üye2 = Üye("Ayşe")
print(kütüphane.kitap_ekle(kitap1))
print(kütüphane.kitap_ekle(kitap2))
print(kütüphane.üye_ekle(üye1))
print(kütüphane.üye_ekle(üye2))
        def kitapları_göster(self):
            return self.__kitapları_göster()
        def üyeleri_göster(self):
            return self.__üyeleri_göster()
print(kütüphane.kitapları_göster())
print(kütüphane.üyeleri_göster())
    def ödünç_alınan_kitapları_göster(self):
        return self.__ödünç_alınan_kitapları_göster()
print(üye1.ödünç_al(kitap1))
print(üye1.ödünç_al(kitap2))
print(üye1.ödünç_alınan_kitapları_göster())
print(üye2.ödünç_al(kitap1))  # Bu kitap zaten ödünç alınmış        