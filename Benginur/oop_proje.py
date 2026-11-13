class Kitap:
    def __init__(self, ad, yazar, isbn):
        self.ad = ad
        self.yazar = yazar
        self.__isbn = isbn  # Kapsülleme (Encapsulation) için private yaptım
        self.oduncte_mi = False

    # ISBN numarasını dışarıdan okuyabilmek için property kullanıyoruz
    @property
    def isbn(self):
        return self.__isbn

    def kitap_bilgisi(self):
        durum = "Ödünç Alındı" if self.oduncte_mi else "Rafta"
        print(f"Kitap: {self.ad} | Yazar: {self.yazar} | Durum: {durum}")


class Uye:
    def __init__(self, isim,uye_id):
        self.isim = isim
        self.uye_id = uye_id
        self.alinan_kitaplar = []

    def kitap_al(self, kitap):
        if not kitap.oduncte_mi:
            kitap.oduncte_mi = True
            self.alinan_kitaplar.append(kitap)
            print(f"[+] {self.isim}, '{kitap.ad}' kitabını başarıyla ödünç aldı.")
        else:
            print(f"[!] '{kitap.ad}' zaten başka bir üyede.")

    def kitap_iade_et(self, kitap):
        if kitap in self.alinan_kitaplar:
            kitap.oduncte_mi = False
            self.alinan_kitaplar.remove(kitap)
            print(f"[-] {self.isim}, '{kitap.ad}' kitabını iade etti.")
        else:
            print("[!] Bu kitap bu üyede kayıtlı görünmüyor.")


# Kalıtım (Inheritance) örneği: OgrenciUye sınıfı Uye sınıfından türuyor
class OgrenciUye(Uye):
    def __init__(self, isim, uye_id, bolum):
        super().__init__(isim, uye_id)
        self.bolum = bolum
        self.max_kitap_limiti = 3  # Öğrenciler en fazla 3 kitap alabilir

    # Method Overriding (Çok biçimlilik)
    def kitap_al(self, kitap):
        if len(self.alinan_kitaplar) >= self.max_kitap_limiti:
            print(f"[!] {self.isim} limitine ulaştı! En fazla {self.max_kitap_limiti} kitap alabilir.")
        else:
            super().kitap_al(kitap)


#  Test Kodu 
if __name__ == "__main__":
    print("--- Kütüphane Sistemi Test Başlıyor ---")
    
    # Nesneleri oluşturuyoruz
    k1 = Kitap("Suç ve Ceza", "Dostoyevski", "9750738481")
    k2 = Kitap("Simyacı", "Paulo Coelho", "9789750514104")
    k3 = Kitap("1984", "George Orwell", "9789750718533")

    # Öğrenci üyemizi oluşturalım
    ogrenci = OgrenciUye("Bengi", 2026, "Bilgisayar Mühendisliği")
    
    print(f"Üye: {ogrenci.isim} ({ogrenci.bolum})\n")

    # Kitap alma işlemleri
    ogrenci.kitap_al(k1)
    ogrenci.kitap_al(k2)
    
    print("\nKitapların güncel durumu:")
    k1.kitap_bilgisi()
    k2.kitap_bilgisi()

    print("\nİade işlemi deneniyor:")
    ogrenci.kitap_iade_et(k1)
    
    print("\nSon durum:")
    k1.kitap_bilgisi()
