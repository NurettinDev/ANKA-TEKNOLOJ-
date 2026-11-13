class Kayit:
    def __init__(self, kayit_id,oncelik,yuk,butunluk):
        self.kayit_id = kayit_id
        self.oncelik= oncelik
        self.yuk=yuk
        self.butunluk=butunluk

    def uygun_mu(self):
        # 1-5 arasınds tam sayı olmalı
        if type(self.oncelik) != int or self.oncelik < 1 or self.oncelik > 5:
            return False, "öncelik 1 ile 5 arasinda tam sayi olmalı"

        # İşlem yükü pozitif tam sayı olmalı
        if type(self.yuk)  != int or self.yuk <= 0:
            return False,"islem yuku pozitif tam sayi olmalı"

        # Bütünlük sağlam olmalı
        if self.butunluk !="sağlam":
            return False, "kayit butunlugu bozuk"

        return True, "uygun"


class YerIstasyonu:
    def __init__(self,kapasite):
        self.kapasite =kapasite
        self.kayitlar = []
    def kayit_ekle(self,kayit):
        self.kayitlar.append(kayit)
    def kayitlari_isle(self):
        islenenler= []
        bekleyenler= []
        reddedilenler= []

        kalan_kapasite = self.kapasite
        kullanilan_kapasite= 0
        kullanilan_idler= []
        uygun_kayitlar= []

        #1.Adım:Kimlik ve bütünlük kontrolü
        for kayit in self.kayitlar:
            if kayit.kayit_id == "" or kayit.kayit_id is None:
                reddedilenler.append((kayit.kayit_id, "Gecersiz kayit kimligi"))
                continue

            if kayit.kayit_id in kullanilan_idler:
                reddedilenler.append((kayit.kayit_id, "Ayni kimlik tekrar kullanilmis"))
                continue

            kullanilan_idler.append(kayit.kayit_id)

            durum,sebep = kayit.uygun_mu()
            if not durum:
                reddedilenler.append((kayit.kayit_id, sebep))
            else:
                uygun_kayitlar.append(kayit)

        # 2.Adım:Önceliğe göre sırala(5 en yüksek,eşitlikte geliş sırası korunur)
        uygun_kayitlar.sort(key=lambda x: x.oncelik,reverse=True)

        # 3.Adım: Kapasite kontrolü yapılır
        for kayit in uygun_kayitlar:
            if kayit.yuk <= kalan_kapasite:
                islenenler.append(kayit)
                kalan_kapasite -= kayit.yuk
                kullanilan_kapasite += kayit.yuk
            else:
                bekleyenler.append(kayit)

        return islenenler, bekleyenler, reddedilenler, kullanilan_kapasite, kalan_kapasite

    def sonucu_yazdir(self, baslik=""):
        if baslik:
            print(f"\n {baslik} ")

        islenenler, bekleyenler, reddedilenler, kullanilan, kalan = self.kayitlari_isle()

        print("Islenenler:", [k.kayit_id for k in islenenler])
        print("Bekleyenler:", [k.kayit_id for k in bekleyenler])

        if reddedilenler:
            red_metni = [f"{kid} ({sebep})" for kid, sebep in reddedilenler]
            print("Reddedilenler:", ", ".join(red_metni))
        else:
            print("Reddedilenler:Yok")

        print(f"Kullanilan kapasite: {kullanilan} | Kalan kapasite: {kalan}")

istasyon = YerIstasyonu(7)
istasyon.kayit_ekle(Kayit("H1", 5, 4, "sağlam"))
istasyon.kayit_ekle(Kayit("H2", 4, 6, "sağlam"))
istasyon.kayit_ekle(Kayit("H3", 4, 3, "sağlam"))
istasyon.kayit_ekle(Kayit("H4", 2, 2, "bozuk"))
istasyon.sonucu_yazdir("Kontrol Ornegi")


#Test 1: Tüm kayıtlar sağlam ve toplam yük kapasite içinde
test1 = YerIstasyonu(15)
test1.kayit_ekle(Kayit("A1", 3, 4, "sağlam"))
test1.kayit_ekle(Kayit("A2", 5, 3, "sağlam"))
test1.kayit_ekle(Kayit("A3", 2, 2, "sağlam"))
test1.sonucu_yazdir("Test 1 - Hepsi Kapasite Icinde")


# Test 2:İki kayıt aynı öncelikte, eklenme sırası bozulmamalı
test2 = YerIstasyonu(5)
test2.kayit_ekle(Kayit("B1", 4, 4, "sağlam"))
test2.kayit_ekle(Kayit("B2", 4, 3, "sağlam"))
test2.sonucu_yazdir("Test 2 - Esit Oncelik Sirasi")


#Test3: Yükü fazla olan beklerken sonraki küçük kayıt işlenebilmeli
test3 = YerIstasyonu(8)
test3.kayit_ekle(Kayit("C1", 5, 7, "sağlam"))
test3.kayit_ekle(Kayit("C2", 4, 5, "sağlam"))
test3.kayit_ekle(Kayit("C3", 3, 1, "sağlam"))
test3.sonucu_yazdir("Test 3 - Kucuk Kaydin Islenmesi")


#Test 4: bütünlüğü bozuk veya geçersiz kayıtler reddedilmeli
test4 = YerIstasyonu(10)
test4.kayit_ekle(Kayit("D1", 5, 2, "bozuk"))
test4.kayit_ekle(Kayit("D2", 7, 2, "sağlam"))
test4.kayit_ekle(Kayit("D3", 3, -4, "sağlam"))
test4.kayit_ekle(Kayit("D1", 4, 2, "sağlam"))
test4.kayit_ekle(Kayit("D4", 3, 4, "sağlam"))
test4.sonucu_yazdir("Test 4 - Hatali ve Bozuk Kayitlar")