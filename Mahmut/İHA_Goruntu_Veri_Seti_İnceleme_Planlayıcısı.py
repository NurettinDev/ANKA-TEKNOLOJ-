'''AD: Mahmut
   PROJE: İHA Görüntü Veri Seti İnceleme Planlayıcısı'''

# Aşağıdaki goruntuGrubu sınıfı her bir görüntü grubunun özelliklerini ve kurallarını temsil etmektedir.

class goruntuGrubu:
    def __init__(self, grupID, oncelik, sure, hazir):
        self.grupID = grupID
        self.oncelik = oncelik
        self.sure = sure
        self.hazir = hazir

    # Aşağıdaki kurallarKontrolleri metodu her bir görüntü grubunun kurallarını kontrol edip ve geçerli olup olmadığını belirlemektedir.

    def kuralKontolleri(self):
        if self.oncelik > 5 or self.oncelik < 1:
            return "Öncelik durumu uygun değildir."
        if self.sure <= 0:
            return "Süre hatalı 0 veya negatif değer olamaz."
        if not self.hazir:
            return "Görüntü grubu verileri eksiktir ve kontrol için uygun değildir."
        return None

# Aşağıdaki talepInceleme sınıfı tüm görüntü gruplarını inceleyip planlama yapacak olan sınıftır. Bu sınıf toplam süreyi ve talepleri saklar ve talepleri değerlendirmektedir.

class talepInceleme:
    def __init__(self, toplamSure):
        self.toplamSure = toplamSure
        self.incelemeTalepleri = []

    # Aşağıdaki talepEkle metodu yeni bir görüntü grubu talebini inceleme taleplerine ekler.

    def talepEkle(self, talep):
        self.incelemeTalepleri.append(talep)

    # Aşağıdaki talepDegerlendirme metodu tüm talepleri değerlendirir ve planlanan, bekleyen ve reddedilen grupları belirler aynı zamanda kullanılan ve kalan süreyi hesaplar.

    def talepDegerlendirme(self):
        planlanan = []
        bekleyen = []
        reddEdilen = []
        kalanSure = self.toplamSure
        kullanilanSure = 0

        gecerliTalepler = []
        goruntulenenler = set()

        for talep in self.incelemeTalepleri:
            if talep.grupID in goruntulenenler:
                reddEdilen.append(talep)
                continue
            goruntulenenler.add(talep.grupID)

            sorun = talep.kuralKontolleri()
            if sorun is not None:
                reddEdilen.append(talep)
            else:
                gecerliTalepler.append(talep)

        gecerliTalepler.sort(key=lambda x: x.oncelik, reverse = True)

        for talep in gecerliTalepler:
            if talep.sure <= kalanSure:
                planlanan.append(talep)
                kalanSure -= talep.sure
                kullanilanSure += talep.sure
            else:
                bekleyen.append(talep)

        print("Planlanan")
        for talep in planlanan:
            print(talep.grupID)

        print("Bekleyenler")
        for talep in bekleyen:
            print(talep.grupID)

        print("Reddedilenler")
        for talep in reddEdilen:
            print(talep.grupID)

        print("Kullanılan Süre:", kullanilanSure, "Dakika")
        print("Kalan Süre:", kalanSure, "Dakika")





'''Test-1:Tüm geçerli grupların inceleme süresine sığması'''

print("-------------------------------------------------------------------------")
print("Test-1: Tüm geçerli grupların inceleme süresine sığması")
T1 = talepInceleme(30)
T1.talepEkle(goruntuGrubu("G1", 3, 10, True))
T1.talepEkle(goruntuGrubu("G2", 2, 15, True))
T1.talepEkle(goruntuGrubu("G3", 1, 5, True))
T1.talepDegerlendirme()
print("-------------------------------------------------------------------------")

'''Test-2:Aynı önceliğe sahip iki grubun doğru sırayla değerlendirilmesi'''

print("Test-2:Aynı önceliğe sahip iki grubun doğru sırayla değerlendirilmesi")
T2 = talepInceleme(10)
T2.talepEkle(goruntuGrubu("G4", 3, 6, True))
T2.talepEkle(goruntuGrubu("G5", 3, 6, True))
T2.talepDegerlendirme()
print("-------------------------------------------------------------------------")

'''Test-3:Büyük bir grup beklerken daha kısa grubun planlanabilmesi'''

print("Test-3:Büyük bir grup beklerken daha kısa grubun planlanabilmesi")
T3 = talepInceleme(12)
T3.talepEkle(goruntuGrubu("G6", 5, 8, True))
T3.talepEkle(goruntuGrubu("G7", 4, 9, True))
T3.talepEkle(goruntuGrubu("G8", 2, 3, True))
T3.talepDegerlendirme()
print("-------------------------------------------------------------------------")

'''Test-4:Hazır olmayan veya geçersiz süreye sahip grupların reddedilmesi'''

print("Test-4:Hazır olmayan veya geçersiz süreye sahip grupların reddedilmesi")
T4 = talepInceleme(10)
T4.talepEkle(goruntuGrubu("G9", 3, 4, False))  
T4.talepEkle(goruntuGrubu("G10", 3, 0, True))
T4.talepEkle(goruntuGrubu("G11", 3, -5, True))
T4.talepEkle(goruntuGrubu("G12", 6, 4, True))
T4.talepEkle(goruntuGrubu("G13", 4, 5, True))
T4.talepEkle(goruntuGrubu("G13", 5, 2, True))
T4.talepDegerlendirme()
print("-------------------------------------------------------------------------")