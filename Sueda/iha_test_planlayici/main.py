from test_senaryosu import TestSenaryosu
from test_planlayici import TestPlanlayici


def senaryo_calistir(baslik, toplam_sure, test_listesi, beklenen):
    print(f"{baslik} (Toplam Sure: {toplam_sure} dk)")
   
    planlayici = TestPlanlayici(toplam_sure)

    for test in test_listesi:
        planlayici.test_ekle(test)

    sonuc = planlayici.planla()
    sonuc.raporu_yazdir()

    gercek = {
        "planlanan": [t.test_id for t in sonuc.planlanan],
        "bekleyen": [t.test_id for t in sonuc.bekleyen],
        "reddedilen": [t.test_id for t in sonuc.reddedilen],
        "kullanilan": sonuc.kullanilan_sure_hesapla(),
        "kalan": sonuc.kalan_sure_hesapla()
    }

    basarili_mi = (gercek == beklenen)
    durum_metni = "BASARILI" if basarili_mi else "BASARISIZ"

    print("\nKontrol:")
    print(f"  Beklenen : {beklenen}")
    print(f"  Gercek   : {gercek}")
    print(f"  Sonuc    : {durum_metni}\n")

    return basarili_mi


def main():
    sonuclar = []

    # ipucundaki örnek senaryo
    ornek_testler = [
        TestSenaryosu("T1", oncelik=5, sure=6, hazir=True),
        TestSenaryosu("T2", oncelik=4, sure=5, hazir=True),
        TestSenaryosu("T3", oncelik=3, sure=4, hazir=True),
        TestSenaryosu("T4", oncelik=2, sure=2, hazir=False)
    ]
    sonuclar.append(senaryo_calistir(
        "Ornek Senaryo",
        toplam_sure=10,
        test_listesi=ornek_testler,
        beklenen={
            "planlanan": ["T1", "T3"],
            "bekleyen": ["T2"],
            "reddedilen": ["T4"],
            "kullanilan": 10,
            "kalan": 0
        }
    ))

    # Senaryo 1:tüm hazır testlerin süreye sığdığı durum
    senaryo_1 = [
        TestSenaryosu("A1", oncelik=3, sure=5, hazir=True),
        TestSenaryosu("A2", oncelik=5, sure=4, hazir=True),
        TestSenaryosu("A3", oncelik=1, sure=6, hazir=True)
    ]
    sonuclar.append(senaryo_calistir(
        "Senaryo 1: Tum Hazir Testlerin Sureye Sigmasi",
        toplam_sure=20,
        test_listesi=senaryo_1,
        beklenen={
            "planlanan": ["A2", "A1", "A3"],
            "bekleyen": [],
            "reddedilen": [],
            "kullanilan": 15,
            "kalan": 5
        }
    ))

    # Senaryo 2:önceliği eşit iki testin geliş sırasının korunması
    senaryo_2 = [
        TestSenaryosu("X1", oncelik=4, sure=4, hazir=True),
        TestSenaryosu("X2", oncelik=4, sure=3, hazir=True),
        TestSenaryosu("X3", oncelik=5, sure=2, hazir=True),
        TestSenaryosu("X4", oncelik=4, sure=5, hazir=True)
    ]
    sonuclar.append(senaryo_calistir(
        "Senaryo 2: Esit Oncelikte Eklenme Sirasinin Korunmasi",
        toplam_sure=10,
        test_listesi=senaryo_2,
        beklenen={
            "planlanan": ["X3", "X1", "X2"],
            "bekleyen": ["X4"],
            "reddedilen": [],
            "kullanilan": 9,
            "kalan": 1
        }
    ))

    # Senaryo 3:uzun bir test beklerken kısa bir testin planlanabilmesi
    senaryo_3 = [
        TestSenaryosu("U1", oncelik=5, sure=6, hazir=True),
        TestSenaryosu("U2", oncelik=4, sure=5, hazir=True),
        TestSenaryosu("U3", oncelik=2, sure=2, hazir=True)
    ]
    sonuclar.append(senaryo_calistir(
        "Senaryo 3: Uzun Test Beklerken Kisa Testin Planlanmasi",
        toplam_sure=8,
        test_listesi=senaryo_3,
        beklenen={
            "planlanan": ["U1", "U3"],
            "bekleyen": ["U2"],
            "reddedilen": [],
            "kullanilan": 8,
            "kalan": 0
        }
    ))

    # Senaryo 4:hazır olmayan,geçersiz veya tekrar eden testler
    senaryo_4 = [
        TestSenaryosu("G1", oncelik=5, sure=4, hazir=True),
        TestSenaryosu("G2", oncelik=4, sure=3, hazir=False),   # hazir degil
        TestSenaryosu("G3", oncelik=3, sure=0, hazir=True),    # gecersiz sure (0)
        TestSenaryosu(" G1 ", oncelik=5, sure=1, hazir=True),  # tekrar eden ID (bosluklu)
        TestSenaryosu("G4", oncelik=7, sure=2, hazir=True),    # gecersiz oncelik (7)
        TestSenaryosu("G5", oncelik=2, sure=3, hazir=True)
    ]
    sonuclar.append(senaryo_calistir(
        "Senaryo 4: Gecersiz ve Tekrar Eden Kayitlarin Reddedilmesi",
        toplam_sure=10,
        test_listesi=senaryo_4,
        beklenen={
            "planlanan": ["G1", "G5"],
            "bekleyen": [],
            "reddedilen": ["G2", "G3", "G1", "G4"],
            "kullanilan": 7,
            "kalan": 3
        }
    ))

    # Senaryo 5 : toplam sürenin 0 olması durumu
    senaryo_5 = [
        TestSenaryosu("S1", oncelik=5, sure=2, hazir=True),
        TestSenaryosu("S2", oncelik=3, sure=1, hazir=False)
    ]
    sonuclar.append(senaryo_calistir(
        "Ek Senaryo: Toplam Surenin 0 Olmasi",
        toplam_sure=0,
        test_listesi=senaryo_5,
        beklenen={
            "planlanan": [],
            "bekleyen": ["S1"],
            "reddedilen": ["S2"],
            "kullanilan": 0,
            "kalan": 0
        }
    ))

    basarili_sayisi = sum(sonuclar)
    print(f"GENEL SONUC: {basarili_sayisi}/{len(sonuclar)} senaryo basarili.")
   
if __name__ == "__main__":
    main()