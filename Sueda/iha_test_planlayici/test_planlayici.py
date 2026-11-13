from test_senaryosu import TestSenaryosu

#bu sınıfta TestPlanlayicinin kararları tutlup ekrana basılıyor
class PlanlamaSonucu:
    def __init__(self, toplam_sure):
        self.toplam_sure = toplam_sure
        self.planlanan = []
        self.bekleyen = []
        self.reddedilen = []

    def planlanan_ekle(self, test, neden):
        test.durum = "planlanan"
        test.neden = neden
        self.planlanan.append(test)

    def bekleyen_ekle(self, test, neden):
        test.durum = "bekleyen"
        test.neden = neden
        self.bekleyen.append(test)

    def reddedilen_ekle(self, test, neden):
        test.durum = "reddedilen"
        test.neden = neden
        self.reddedilen.append(test)

    def kullanilan_sure_hesapla(self):
        toplam = 0
        for test in self.planlanan:
            toplam += test.sure
        return toplam

    def kalan_sure_hesapla(self):
        return self.toplam_sure - self.kullanilan_sure_hesapla()

    def _id_listesi_metni(self, liste):
        if not liste:
            return "Yok"
        return ", ".join(str(t.test_id) for t in liste)

    def raporu_yazdir(self):
        kullanilan = self.kullanilan_sure_hesapla()
        kalan = self.kalan_sure_hesapla()

        print(f"Planlanan       : {self._id_listesi_metni(self.planlanan)}")
        print(f"Bekleyen        : {self._id_listesi_metni(self.bekleyen)}")
        print(f"Reddedilen      : {self._id_listesi_metni(self.reddedilen)}")
        print(f"Kullanilan sure : {kullanilan} dakika")
        print(f"Kalan sure      : {kalan} dakika")

        print("\nKarar Detaylari:")
        for grup_adi, liste in [
            ("Planlanan", self.planlanan),
            ("Bekleyen", self.bekleyen),
            ("Reddedilen", self.reddedilen)
        ]:
            for t in liste:
                print(f"  [{grup_adi}] {t.test_id} -> {t.neden}")


class TestPlanlayici:
    def __init__(self, toplam_sure):
        if type(toplam_sure) is not int or toplam_sure < 0:
            raise ValueError("sure negatif olamaz")

        self.toplam_sure = toplam_sure
        self.gecerli_testler = []
        self.reddedilen_testler = []
        self.gorulen_idler = set()
        self.eklenen_nesneler = set()
        self.sayac = 0

    def test_ekle(self, test):
        if not isinstance(test, TestSenaryosu):
            raise TypeError("yalnizca TestSenaryosu nesneleri eklenebilir")

        if id(test) in self.eklenen_nesneler:
            raise ValueError("ayni test nesnesini bir daha ekleyemezsin")
        self.eklenen_nesneler.add(id(test))

        self.sayac += 1
        test.sira_no = self.sayac

        # aynı test idsinin bir daha eklenmesini engelliyor
        if type(test.test_id) is str and test.test_id in self.gorulen_idler:
            neden = "Tekrar eden test kimligi"
            test.durum = "reddedilen"
            test.neden = neden
            self.reddedilen_testler.append((test, neden))
            return

        if type(test.test_id) is str and test.test_id != "":
            self.gorulen_idler.add(test.test_id)

        # test kuralları sağlıyor mu
        gecerli_mi, mesaj = test.dogrula()
        if not gecerli_mi:
            test.durum = "reddedilen"
            test.neden = mesaj
            self.reddedilen_testler.append((test, mesaj))
            return

        self.gecerli_testler.append(test)

    def planla(self):
        sonuc = PlanlamaSonucu(self.toplam_sure)

        # elenen testleri sonuç nesnesine ekle
        for test, neden in self.reddedilen_testler:
            sonuc.reddedilen_ekle(test, neden)

        
        sirali_testler = sorted(
            self.gecerli_testler,
            key=lambda t: (-t.oncelik, t.sira_no)
        )

        kalan_sure = self.toplam_sure
        for test in sirali_testler:
            if test.sure <= kalan_sure:
                kalan_sure -= test.sure
                sonuc.planlanan_ekle(
                    test,
                    f"Sureye sigdi (Oncelik: {test.oncelik}, Sure: {test.sure} dk, Kalan: {kalan_sure} dk)"
                )
            else:
                # sığmayan testler beklemede
                sonuc.bekleyen_ekle(
                    test,
                    f"Sure yetersiz (Gereken: {test.sure} dk, Kalan: {kalan_sure} dk)"
                )

        return sonuc
