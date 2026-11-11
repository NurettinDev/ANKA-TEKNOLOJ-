"""""
Algoritma Açıklaması:
1.İstek sınıfını ve ödevde istenilen özellikleri tanımladım.(kimlik,oncelik,adet,yetki,durum,neden)
2.Olarak Deponun sınıfını ve ödevde istenilen özellikleri tanımladım.(kapasite,kalan_kapasite,istekler)
3.İstekleri istekler[] listesine eklemek için istek_ekle() fonksiyonunu tanımladım.
4.Olarak istekler[] listesindeki istekleri değerlendirmek için istek_degerlendir() fonksiyonunu tanımladım.
4.1.İsteklerin kimlik tekrarını kontrol ettim ve tekrar eden istekleri reddettim.
4.2.İsteklerin yetkisini kontrol ettim ve yetkisiz istekleri reddettim.
4.3.İsteklerin öncelik değerlerini kontrol ettim ve geçersiz öncelik değerlerini reddettim.
4.4.İsteklerin öncelik değerlerini büyükten küçüğe sıralamak için 5'ten 1'e doğru sayan bir döngü kurdum.
Her öncelik değeri için uygunlar[] listesini baştan gezdim ve o önceliğe sahip istekleri sirali_uygunlar[] listesine ekledim.
Liste her seferinde baştan gezildiği için eşit öncelikli isteklerde önce eklenen istek önce değerlendirilmiş oldu.
4.5.Uygn_siralı_uygunlar[] listesindeki isteklerin adet değerlerini kontrol ettim.
Burdan adet değeri geçersiz olan istekleri reddettim.Diğer isteklerin kalan kapasiteye göre onaylama veya bekletme işlemini yaptım.
5.İsteklerin durumlarını ve nedenlerini raporlamak için raporla() fonksiyonunu tanımladım.
6.Test senaryolarını oluşturdum ve beklenen sonuçları ile gerçek sonuçları karşılaştırdım.


"""
class istek:                                        #Burda istek sınıfını tanımladım ve gerekli özellikleri ekledim            
    def __init__(self,kimlik,oncelik,adet,yetki):
        self.kimlik = kimlik
        self.oncelik = oncelik
        self.adet = adet
        self.yetki = yetki
        self.durum=""                               
        self.neden=""
i=0
j=0
k=0
class depo:                                           #Burda depo sınıfını tanımladım ve gerekli özellikleri ekledim
    def __init__(self,kapasite):
        self.kapasite = kapasite
        self.kalan_kapasite = kapasite
        self.istekler = []                      

    def istek_ekle(self,istek):
        self.istekler.append(istek)                     #İstekleri listeye ekledim

    def istek_degerlendir(self):
        uygunlar=[]                             
        sirali_uygunlar=[]
        gorulen_kimlikler=[]
        for i in range(len(self.istekler)):
            if self.istekler[i].kimlik not in gorulen_kimlikler:        #Kimlik Tekrarını Kontrol Ettim
                gorulen_kimlikler.append(self.istekler[i].kimlik)       
                if (self.istekler[i].yetki == True):                    #Yetki Kontrolü
                    uygunlar.append(self.istekler[i])
                else:
                    self.istekler[i].durum="Reddedildi"                 
                    self.istekler[i].neden="Yetkisiz"
            else:
                self.istekler[i].durum="Reddedildi"                                     
                self.istekler[i].neden="Aynı kimlikli istek daha önce gönderilmiş"       
        for oncelik in range(5,0,-1):                                                             #Öncelik Sırasının oluşturulması
                            for j in range(len(uygunlar)):
                                if(uygunlar[j].oncelik == oncelik and (uygunlar[j].oncelik<=5 and uygunlar[j].oncelik>0)):
                                    sirali_uygunlar.append(uygunlar[j])                             #Oncelik sırasına göre büyükten küçüğe doğru "sirali_uygunlar" listesine ekledim
                                elif(uygunlar[j].oncelik>5 or uygunlar[j].oncelik<=0):              #Sınır dışı öncelik değerlerini kontrol ettim ve reddedilen istekleri işaretledim
                                    uygunlar[j].durum="Reddedildi"
                                    uygunlar[j].neden="Geçersiz öncelik değeri"    
        for k in range(len(sirali_uygunlar)):                                                        #Adet Kontrolü ve Kalan Kapasiteye Göre Onaylama veya Bekletme İşlemi   
            if (self.kalan_kapasite >= sirali_uygunlar[k].adet and sirali_uygunlar[k].adet>0):
                self.kalan_kapasite -= sirali_uygunlar[k].adet                                       #Onaylanan isteğin adeti kadar kalan kapasiteyi düşürdüm
                sirali_uygunlar[k].durum="Onaylandı"
                sirali_uygunlar[k].neden="Yeterli kapasite var"
            elif(sirali_uygunlar[k].adet<=0):
                sirali_uygunlar[k].durum="Reddedildi"                                                  #Geçersiz adet değerlerini kontrol ettim ve reddedilen istekleri işaretledim
                sirali_uygunlar[k].neden="Geçersiz adet değeri"
            else:
                sirali_uygunlar[k].durum="Beklemede"                                                   #Kalan kapasite yetersiz olan istekleri beklemede olarak işaretledim
                sirali_uygunlar[k].neden="Yeterli kapasite yok"
    def raporla(self):                                                                                  #Raporlama Fonksiyonu
        print(f"Dağıtılan Kapasite: {self.kapasite-self.kalan_kapasite}, Kalan Kapasite: {self.kalan_kapasite}")
        for i in range(len(self.istekler)):
            print(f"Kimlik: {self.istekler[i].kimlik}, Öncelik: {self.istekler[i].oncelik}, Adet: {self.istekler[i].adet}, Yetki: {self.istekler[i].yetki}, Durum: {self.istekler[i].durum}, Neden: {self.istekler[i].neden}")


print(" Test 1: Hepsi yetkili ve stok yeterli  ")                                          #Test 1: Hepsi yetkili ve stok yeterli
print("Beklenen: T1, T2, T3 onaylandı  Dağıtılan: 9  Kalan: 1")
test1 = depo(10)
T1 = istek("T1", 3, 2, True)
test1.istek_ekle(T1)
T2 = istek("T2", 2, 3, True)
test1.istek_ekle(T2)
T3 = istek("T3", 1, 4, True)
test1.istek_ekle(T3)
test1.istek_degerlendir()
test1.raporla()


# Test 1 Sonuc 
#  Test 1: Hepsi yetkili ve stok yeterli 
# Beklenen: T1, T2, T3 onaylandı  Dağıtılan: 9  Kalan: 1
# Dağıtılan Kapasite: 9, Kalan Kapasite: 1
# Kimlik: T1, Öncelik: 3, Adet: 2, Yetki: True, Durum: Onaylandı, Neden: Yeterli kapasite var
# Kimlik: T2, Öncelik: 2, Adet: 3, Yetki: True, Durum: Onaylandı, Neden: Yeterli kapasite var
# Kimlik: T3, Öncelik: 1, Adet: 4, Yetki: True, Durum: Onaylandı, Neden: Yeterli kapasite var
# Sonuç: Beklenen ile gerçek sonuç uyuşuyor.


print("\n Test 2: Eşit öncelikte önce eklenen önce değerlendirilir ")                      #Test 2: Eşit öncelikte önce eklenen önce değerlendirilir
print("Beklenen: K1 onaylandı, K2 beklemede  Dağıtılan: 4  Kalan: 1")
test2 = depo(5)
K1 = istek("K1", 3, 4, True)
test2.istek_ekle(K1)
K2 = istek("K2", 3, 4, True)
test2.istek_ekle(K2)
test2.istek_degerlendir()
test2.raporla()


# Test 2 Sonuc
#  Test 2: Eşit öncelikte önce eklenen önce değerlendirilir 
# Beklenen: K1 onaylandı, K2 beklemede  Dağıtılan: 4  Kalan: 1
# Dağıtılan Kapasite: 4, Kalan Kapasite: 1
# Kimlik: K1, Öncelik: 3, Adet: 4, Yetki: True, Durum: Onaylandı, Neden: Yeterli kapasite var
# Kimlik: K2, Öncelik: 3, Adet: 4, Yetki: True, Durum: Beklemede, Neden: Yeterli kapasite yok
# Sonuç: Beklenen ile gerçek sonuç uyuşuyor.


print("\n Test 3: Büyük istek beklerken küçük istek kalan stoğu kullanır ")             #Test 3: Büyük istek beklerken küçük istek kalan stoğu kullanır
print("Beklenen: B1, B3 onaylandı, B2 beklemede, B4 reddedildi  Dağıtılan: 7  Kalan: 0")
test3 = depo(7)
B1 = istek("B1", 5, 5, True)
test3.istek_ekle(B1)
B2 = istek("B2", 4, 4, True)
test3.istek_ekle(B2)
B3 = istek("B3", 3, 2, True)
test3.istek_ekle(B3)
B4 = istek("B4", 2, 1, False)
test3.istek_ekle(B4)
test3.istek_degerlendir()
test3.raporla()


# Test 3 Sonuc
#  Test 3: Büyük istek beklerken küçük istek kalan stoğu kullanır 
# Beklenen: B1, B3 onaylandı, B2 beklemede, B4 reddedildi  Dağıtılan: 7  Kalan: 0
# Dağıtılan Kapasite: 7, Kalan Kapasite: 0
# Kimlik: B1, Öncelik: 5, Adet: 5, Yetki: True, Durum: Onaylandı, Neden: Yeterli kapasite var
# Kimlik: B2, Öncelik: 4, Adet: 4, Yetki: True, Durum: Beklemede, Neden: Yeterli kapasite yok
# Kimlik: B3, Öncelik: 3, Adet: 2, Yetki: True, Durum: Onaylandı, Neden: Yeterli kapasite var
# Kimlik: B4, Öncelik: 2, Adet: 1, Yetki: False, Durum: Reddedildi, Neden: Yetkisiz
# Sonuç: Beklenen ile gerçek sonuç uyuşuyor.


print("\n Test 4: Yetkisiz ve negatif adetli istekler reddedilir ")                       #Test 4: Yetkisiz ve negatif adetli istekler reddedilir
print("Beklenen: R1, R2 reddedildi, R3 onaylandı | Dağıtılan: 3  Kalan: 7")
test4 = depo(10)
R1 = istek("R1", 3, 2, False)
test4.istek_ekle(R1)
R2 = istek("R2", 3, -2, True)
test4.istek_ekle(R2)
R3 = istek("R3", 2, 3, True)
test4.istek_ekle(R3)
test4.istek_degerlendir()
test4.raporla()


#Test 4 Sonuc
#  Test 4: Yetkisiz ve negatif adetli istekler reddedilir 
# Beklenen: R1, R2 reddedildi, R3 onaylandı  Dağıtılan: 3  Kalan: 7
# Dağıtılan Kapasite: 3, Kalan Kapasite: 7
# Kimlik: R1, Öncelik: 3, Adet: 2, Yetki: False, Durum: Reddedildi, Neden: Yetkisiz
# Kimlik: R2, Öncelik: 3, Adet: -2, Yetki: True, Durum: Reddedildi, Neden: Geçersiz adet değeri
# Kimlik: R3, Öncelik: 2, Adet: 3, Yetki: True, Durum: Onaylandı, Neden: Yeterli kapasite var
# Sonuç: Beklenen ile gerçek sonuç uyuşuyor.










    