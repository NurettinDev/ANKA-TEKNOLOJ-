

class Gorev:

    """Tek bir görevin kimliğini, önceliğini, süresini ve uçuş uygunluğunu tutan sınıf."""
    def __init__(self, gorev_id, oncelik, sure, uygunluk=True):
        self.gorev_id = gorev_id        # Görevin benzersiz kimliğidir.
        self.oncelik = oncelik           # Görevin öncelik derecesidir.
        self.sure = sure                # Görevin harcayacağı dakikadır.
        self.uygunluk = uygunluk        # Uçuşa uygun mu? kontrolü yapılmalı.
        self.durum = None             # Sonradan netleşecek: 'kabul edildi', 'bekliyor', 'reddedildi'
        self.red_nedeni = ""              # Reddedildiyse veya bekletildiyse nedeninini belirleyecek.


class UcusPlanlayici:
    """Görevleri kurallara göre değerlendiren ve uçuş planını çıkaran sınıf."""
    def __init__(self, toplam_kapasite):
        self.toplam_kapasite = toplam_kapasite           # Uçuş için verilen toplam dakika limitidir.
        self.kalan_kapasite = toplam_kapasite          # İşlem yaptıkça azalcak olan kalan süredir.
        self.gorevler = []                            #Eklenen tüm görevlerin saklandığı listedir.
        self.id_kumesi = set()                                 # Aynı ID'den birden fazla eklenmesini engellemek için küme oluşturdum.
        self.ekleme_sirasi = 0                          # Eşit öncelikli görevlerde "önce gelen önce alınır" kuralı için sayaç oluşturdum

    def gorev_ekle(self, gorev_id, oncelik, sure, uygunluk=True):

        # Tekrar Eden ID kontrolü

        if gorev_id in self.id_kumesi:
            print(f"[UYARI] '{gorev_id}' ID'li kayıt zaten mevcut. Tekrar eden ID reddedildi.")
            return

        red_nedeni = ""
        GecerliMi = True

            #Veri tipi ve sınır kontrolleri

        if not gorev_id or not isinstance(gorev_id, str):
            red_nedeni = "Geçersiz veya boş kimlik bilgisi."
            GecerliMi = False

        elif not (isinstance(oncelik, int) and 1 <= oncelik <= 5):
            red_nedeni = f"Öncelik ({oncelik}) 1 ile 5 arasında bir tam sayı olmalıdır."
            GecerliMi = False

        elif not (isinstance(sure, int) and sure > 0):
            red_nedeni = f"Süre ({sure}) pozitif bir tam sayı olmalıdır."
            GecerliMi = False

        elif not uygunluk:
            red_nedeni = "Görev uçuşa uygun değil."
            GecerliMi = False

          # Görevi nesne olarak oluşturdum.

        yeni_gorev = Gorev(gorev_id, oncelik, sure, uygunluk)
        self.id_kumesi.add(gorev_id)
        yeni_gorev. sira = self.ekleme_sirasi  # Eşit öncelik için FIFO takibi
        self.ekleme_sirasi += 1

        # Yukarıda bir kural ihlali olduysa direkt 'reddedildi'olur

        if not GecerliMi:
            yeni_gorev.durum = 'reddedildi'
            yeni_gorev.red_nedeni = red_nedeni

        self.gorevler.append(yeni_gorev)

    def planlamayi_baslat(self):
        # Sadece geçerli ve uygun olan görevleri işleme alacağız
        aktif_gorevler = [g for g in self.gorevler if g.durum != 'reddedildi']

           # Sıralama Kuralı: 
        # 1. Önceliği yüksek olan önce olur.(5'ten 1'e doğru azalandır.)
        # 2. Öncelikler eşitse sisteme önce eklenen önce (ekleme sırasına göre artan olarak yapacağız.)

        aktif_gorevler.sort(key=lambda x: (-x.oncelik, x.sira))

        self.kalan_kapasite = self.toplam_kapasite

        for g in aktif_gorevler:
            if g.sure <= self.kalan_kapasite:
                g.durum = 'kabul edildi'
                self.kalan_kapasite -= g.sure
            else:
                g.durum = 'bekliyor'
                g.red_nedeni = 'Kalan uçuş kapasitesi yetersiz.'

    def rapor_yazdir(self, senaryo_adi):
        print(f"\n= {senaryo_adi} =")
        print(f"Toplam Kapasite: {self.toplam_kapasite} dk | Kullanılan: {self.toplam_kapasite - self.kalan_kapasite} dk | Kalan: {self.kalan_kapasite} dk")
        
        kabul = [g.gorev_id for g in self.gorevler if g.durum == 'kabul edildi']
        bekleyen = [g.gorev_id for g in self.gorevler if g.durum == 'bekliyor']
        reddedilen = [g for g in self.gorevler if g.durum == 'reddedildi']

        print(f"Uçuşa Alınanlar : {', '.join(kabul) if kabul else 'Yok'}")
        print(f"Bekleyenler     : {', '.join(bekleyen) if bekleyen else 'Yok'}")
        
        print("Reddedilenler ve Nedenleri:")
        if reddedilen:
            for g in reddedilen:
                print(f"  - {g.gorev_id}: {g.red_nedeni}")
        else:
            print("  - Yok")
        print("---")


#  TEST SENARYOLARI 
if __name__ == "__main__":
    
           # Test Senaryosu 1: Tüm görevler uygun ve süre toplamı limitin altında
    s1 = UcusPlanlayici(toplam_kapasite=15)
    s1.gorev_ekle("G1", 3, 4, True)
    s1.gorev_ekle("G2", 5, 5, True)
    s1.gorev_ekle("G3", 4, 3, True)
    s1.planlamayi_baslat()
    s1.rapor_yazdir("TEST 1: Hepsi Uygun ve Sığar")

           # Test Senaryosu 2: Eşit öncelikli görevlerin eklenme sırası korunmalı 
    s2 = UcusPlanlayici(toplam_kapasite=6)
    s2.gorev_ekle("A1", 4, 4, True)  # Önce ekleniyor
    s2.gorev_ekle("A2", 4, 4, True)  # Sonra ekleniyor (sığmayacak, bekleyecek)
    s2.planlamayi_baslat()
    s2.rapor_yazdir("TEST 2: Eşit Öncelik ve Sıralama Korunumu")

         # Test Senaryosu 3: Uzun görev beklerken daha kısa sonraki görevin alınabilmesi
    s3 = UcusPlanlayici(toplam_kapasite=5)
    s3.gorev_ekle("B1", 5, 8, True)  # Yüksek öncelikli ama kapasiteye sığmıyor bu yüzden bekliyor
    s3.gorev_ekle("B2", 3, 3, True)  # Düşük öncelikli ama kalan kapasiteye sığıyor  bu yüzden kabul
    s3.planlamayi_baslat()
    s3.rapor_yazdir("TEST 3: Uzun Görev Beklerken Kısa Görevin Alınması")

            # Test Senaryosu 4: Uçuşa uygun olmayan, süresi sıfır olan veya hatalı kayıtlar
    s4 = UcusPlanlayici(toplam_kapasite=10)
    s4.gorev_ekle("X1", 4, 0, True)   # Süresi sıfır bundan dolayı reddedilmeli
    s4.gorev_ekle("X2", 6, 4, True)   # Önceliği aralık dışı (6) bu yüzden reddedilmeli
    s4.gorev_ekle("X3", 2, 3, False)  # Uygun değil bundan dolayı reddedilmeli
    s4.planlamayi_baslat()
    s4.rapor_yazdir("TEST 4: Hatalı ve Uygun Olmayan Kayıtlar")

    """

 
 Algoritma Açıklaması:
   Geliştirilen sistemde öncelikle tüm görevler veri bütünlüğü,  pozitif süre, 1-5 arası öncelik ve uçuşa uygunluk açısından 
denetleniyor; kural dışı kayıtlar doğrudan 'reddediliyor'. Geçerli kayıtlar, önceliği yüksek olandan düşük olana doğru,önceliklerin eşit olduğu durumlarda
olduğu durumlarda ise sisteme ilk eklenen önce işlenecek şekilde yani (FIFO) mantığıyla sıralanıyor. Ardından kalan uçuş süresi kapasitesi kontrol edilerek
 sıradaki görevin sığması  durumunda uçuşa dahil ediliyor, sığmayan uygun görevler ise 
 daha sonraki küçük görevlerin değerlendirilebilmesi için döngü bozulmadan 'bekliyor' durumuna alınıyor.
 


"""

