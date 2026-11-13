import random

class Veri:
    def __init__(self, kimlik, oncelik, yuk, olcum, sira):
        self.kimlik = kimlik#verinin ismi
        self.oncelik = oncelik#1-5 arasında olan önceliği belirlemek
        self.yuk = yuk#verinin kapladığı kapasite
        self.olcum = olcum#sensörden gelen verinin değeri
        self.sira = sira # Rastgele geliş sırasını takip etmek için
        
    def __str__(self):
        return f"Geliş Sırası: {self.sira} | Kimlik: {self.kimlik} | Öncelik: {self.oncelik} | Yük: {self.yuk} | Ölçüm: {self.olcum}"#anlaşılır şekilde görülmesi için

# Ham veriler
ham_veriler = [
    {"kimlik": "S1", "öncelik": 5, "yük": 4, "ölçüm": 55},
    {"kimlik": "S2", "öncelik": 3, "yük": 3, "ölçüm": 70},
    {"kimlik": "S2", "öncelik": 3, "yük": 3, "ölçüm": 70},  
    {"kimlik": "S3", "öncelik": 6, "yük": 5, "ölçüm": 40},  
    {"kimlik": "S4", "öncelik": 5, "yük": -2, "ölçüm": 35},  
    {"kimlik": "S5", "öncelik": 1, "yük": 8, "ölçüm": 80},
    {"kimlik": "S6", "öncelik": 4, "yük": 5, "ölçüm": 20}, 
    {"kimlik": "S7", "öncelik": 3, "yük": 2, "ölçüm": 95},
    {"kimlik": "S8", "öncelik": 1, "yük": 3, "ölçüm": 120},  
    {"kimlik": "S9", "öncelik": 4, "yük": 11, "ölçüm": 85},
    {"kimlik": "S10", "öncelik": 4, "yük": 4, "ölçüm": 55},  
]

MaxKapasite = 10  # Kapasite sınırı

# Ham verileri RASTGELE karıştırarak sisteme geliş sırasını rastgele yapıyoruz
rastgele_gelen_veriler = random.sample(ham_veriler, len(ham_veriler))

#Bölümlerine göre ayırmak için listeler oluşturuldu
gecerli_adaylar = []#reddedilmeyenlerin tutulduğu liste
reddedilen_veriler = []#şartları geçemeyenlerin tutlduğu liste

gorulen_kimlikler = set()#yinelenen kimlikleri çıkartmak için:set yinelemeye izin vermez

# Rastgele gelen verileri sırayla kontrol edip filtreliyoruz
for sira_no, v in enumerate(rastgele_gelen_veriler, start=1):
    kimlik = v["kimlik"]
    oncelik = v["öncelik"]
    yuk = v["yük"]
    olcum = v["ölçüm"]
    
    # Tekrar eden kimlik kontrolü:kimliği aynı olanları atlayıp geri kalanları, diğer işlemlerde kullanmak için yeniler
    if kimlik in gorulen_kimlikler:
        reddedilen_veriler.append((v, "Tekrar eden kimlik"))
        continue
    gorulen_kimlikler.add(kimlik)
    
    # Öncelik 1-5 aralığı kontrolü:1-5 arasında değilse veya sayı değilse reddedilenlere ekleme yapar
    if not (isinstance(oncelik, (int, float)) and 1 <= oncelik <= 5):
        reddedilen_veriler.append((v, "Öncelik sayı değil ya da 1-5 aralığında değil"))
        continue
        
    # Yükün sayı olmamasını, 0/negatif olmasını veya kapasiteyi aşmasının kontrolü:pozitif sayı değilse yada max kapasiteyi aşıyorsa reddedilenlere eklenir
    if not isinstance(yuk, (int, float)) or yuk <= 0 or yuk > MaxKapasite:
        reddedilen_veriler.append((v, "Yük geçersiz (Pozitif tam sayı değil ya da toplam kapasiteden büyük)"))
        continue
        
    # Ölçüm sayı ve 0-100 aralığı kontrolü:sayı değilse veya 0-100 aralığında değilse reddedilenlere ekler 
    if not isinstance(olcum, (int, float)) or not (0 <= olcum <= 100):
        reddedilen_veriler.append((v, "Ölçüm sayı değil veya 0-100 aralığında değil"))
        continue
    
    #Geri kalanlar için; 
    # Kuralları geçenleri aday listesine ekliyoruz (rastgele geliş sırasını 'sira_no' olarak kaydediyoruz)
    gecerli_adaylar.append(Veri(kimlik, oncelik, yuk, olcum, sira_no))


#  Önceliğe göre sıralama (Önceliği yüksek olan öne geçer, öncelikler eşitse rastgele gelen ilk kazanır)
gecerli_adaylar.sort(key=lambda x: (-x.oncelik, x.sira))# ilk gelen ve en yüksek önceliğe sahip veriler listenin en başına sıralanır


# Kapasite Yönetimi
harcanan_kapasite = 0

kabul_edilenler = []
bekleyenler = []
#harcanan kapasite hesaplanır kapasite daha fazla almaycacak hale gelirse kalanlar bekleyen listesine eklenir
for item in gecerli_adaylar:
    if harcanan_kapasite + item.yuk <= MaxKapasite:
        kabul_edilenler.append(item)
        harcanan_kapasite += item.yuk
    else:
        bekleyenler.append(item)


print(f"\n KABUL EDİLENLER (Toplam: {len(kabul_edilenler)}):")
for item in kabul_edilenler:
    print(f"Kimlik: {item.kimlik} | Öncelik: {item.oncelik} | Yük: {item.yuk} | Ölçüm: {item.olcum} (Geliş Sırası: {item.sira})")

print(f"\n BELEYENLER - Kapasite Yetersiz (Toplam: {len(bekleyenler)}):")
for item in bekleyenler:
    print(f"Kimlik: {item.kimlik} | Öncelik: {item.oncelik} | Yük: {item.yuk} | Ölçüm: {item.olcum} (Geliş Sırası: {item.sira})")

print(f"\n REDDEDİLENLER (Toplam: {len(reddedilen_veriler)}):")
for veri_dict, sebep in reddedilen_veriler:
    print(f"Kimlik: {veri_dict['kimlik']} | Sebep: {sebep}")

kalan_kapasite = MaxKapasite - harcanan_kapasite

print(f"\nKAPASİTE DURUMU:")
print(f"Maksimum Kapasite : {MaxKapasite}")
print(f"Harcanan Kapasite  : {harcanan_kapasite}")
print(f"Kalan Kapasite     : {kalan_kapasite}")
