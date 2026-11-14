"""Yer istasyonu yedekleme talepleri için kapasite planlama simülasyonu.

Gerçek dosya kopyalamaz. Her tur için verilen yeni MB kotasıyla karar verir.
"""


class YedeklemeTalebi:
    """Tek bir dosyanın yedekleme isteğine ait bilgileri tutar."""

    def __init__(self, kimlik, oncelik, gerekli_alan, saglamlik):
        self.kimlik = kimlik
        self.oncelik = oncelik
        self.gerekli_alan = gerekli_alan
        self.saglamlik = saglamlik
        self.eklenme_sirasi = None
        self.durum = None
        self.neden = ""


class YedeklemePlanlayici:
    """Talepleri doğrular, sıraya koyar ve tur kotasına göre değerlendirir."""

    def __init__(self):
        self.talepler = []
        self.bekleyen_talepler = []
        self._gorulen_kimlikler = set()
        self._gorulen_nesneler = set()
        self._yeni_reddedilenler = []
        self.tur_sayisi = 0

    def talep_ekle(self, talep):
        """Talebi bir kez kaydeder; geçersiz veya bozuk olanı reddeder."""
        if not isinstance(talep, YedeklemeTalebi):
            raise TypeError("Yalnızca YedeklemeTalebi nesnesi eklenebilir.")
        if id(talep) in self._gorulen_nesneler:
            raise ValueError("Aynı talep nesnesi ikinci kez eklenemez.")

        self._gorulen_nesneler.add(id(talep))
        talep.eklenme_sirasi = len(self.talepler)
        self.talepler.append(talep)

        red_nedeni = self._red_nedeni_bul(talep)
        if red_nedeni:
            talep.durum = "reddedildi"
            talep.neden = red_nedeni
            self._yeni_reddedilenler.append(talep)
            return False

        self.bekleyen_talepler.append(talep)
        return True

    def _red_nedeni_bul(self, talep):
        if not isinstance(talep.kimlik, str) or not talep.kimlik.strip():
            return "Kimlik boş veya geçersiz."

        talep.kimlik = talep.kimlik.strip()
        if talep.kimlik in self._gorulen_kimlikler:
            return "Kimlik daha önce kullanılmış."
        self._gorulen_kimlikler.add(talep.kimlik)

        if type(talep.oncelik) is not int or not 1 <= talep.oncelik <= 5:
            return "Öncelik 1 ile 5 arasında bir tam sayı olmalı."
        if type(talep.gerekli_alan) is not int or talep.gerekli_alan <= 0:
            return "Gerekli alan pozitif bir tam sayı olmalı."
        if not isinstance(talep.saglamlik, str):
            return "Dosya sağlamlığı geçersiz."

        durum = talep.saglamlik.strip().lower()
        if durum == "bozuk":
            return "Dosya bozuk olduğu için yedeklenemez."
        if durum != "sağlam":
            return "Dosya sağlamlığı 'sağlam' veya 'bozuk' olmalı."
        return ""

    def tur_calistir(self, kapasite):
        """Bir turu bitirir ve sığmayan talepleri sonraki tura bırakır.

        Her çağrıda yeni bir tur kotası verilir. Kabul edilen talepler
        sonraki turda tekrar değerlendirilmez.
        """
        if type(kapasite) is not int or kapasite < 0:
            raise ValueError("Tur kapasitesi negatif olmayan bir tam sayı olmalı.")

        self.tur_sayisi += 1
        kalan = kapasite
        kabul_edilenler = []
        sonraki_tura_kalanlar = []

        sirali_talepler = sorted(
            self.bekleyen_talepler,
            key=lambda talep: (-talep.oncelik, talep.eklenme_sirasi),
        )
        for talep in sirali_talepler:
            if talep.gerekli_alan <= kalan:
                onceki_kalan = kalan
                kalan -= talep.gerekli_alan
                talep.durum = "kabul edildi"
                talep.neden = (
                    f"Öncelik {talep.oncelik} ile değerlendirildi; "
                    f"{talep.gerekli_alan} MB, kalan {onceki_kalan} MB alana sığdı."
                )
                kabul_edilenler.append(talep)
            else:
                talep.durum = "bekliyor"
                talep.neden = (
                    f"{talep.gerekli_alan} MB gerekli, {kalan} MB kaldı; "
                    "sonraki tura aktarıldı."
                )
                sonraki_tura_kalanlar.append(talep)

        self.bekleyen_talepler = sonraki_tura_kalanlar
        rapor = {
            "tur": self.tur_sayisi,
            "kapasite": kapasite,
            "kabul_edilenler": tuple((t.kimlik, t.neden) for t in kabul_edilenler),
            "bekleyenler": tuple((t.kimlik, t.neden) for t in self.bekleyen_talepler),
            "reddedilenler": tuple((t.kimlik, t.neden) for t in self._yeni_reddedilenler),
            "kullanilan": kapasite - kalan,
            "kalan": kalan,
        }
        self._yeni_reddedilenler.clear()

        assert rapor["kullanilan"] == sum(t.gerekli_alan for t in kabul_edilenler)
        assert 0 <= rapor["kullanilan"] <= kapasite
        assert rapor["kullanilan"] + rapor["kalan"] == kapasite
        assert all(t.durum in {"kabul edildi", "bekliyor", "reddedildi"} for t in self.talepler)
        return rapor


def rapor_yazdir(rapor):
    """Bir turun kararlarını nedenleri ve kapasite hesabıyla gösterir."""
    print(f"\n{rapor['tur']}. TUR | Kapasite: {rapor['kapasite']} MB")
    for baslik, anahtar in (
        ("Yedeklenenler", "kabul_edilenler"),
        ("Bekleyenler", "bekleyenler"),
        ("Reddedilenler", "reddedilenler"),
    ):
        print(f"{baslik}:")
        if not rapor[anahtar]:
            print("  Yok")
        for kimlik, neden in rapor[anahtar]:
            print(f"  {kimlik or '<boş kimlik>'}: {neden}")
    print(f"Kullanılan: {rapor['kullanilan']} MB | Kalan: {rapor['kalan']} MB")


if __name__ == "__main__":
    planlayici = YedeklemePlanlayici()
    for talep in (
        YedeklemeTalebi("D1", 5, 6, "sağlam"),
        YedeklemeTalebi("D2", 4, 4, "sağlam"),
        YedeklemeTalebi("D3", 3, 3, "sağlam"),
        YedeklemeTalebi("D4", 2, 2, "bozuk"),
    ):
        planlayici.talep_ekle(talep)

    rapor_yazdir(planlayici.tur_calistir(9))
    # İkinci tur, ödevde zorunlu olmayan bekleyen-kuyruğu örneğidir.
    rapor_yazdir(planlayici.tur_calistir(5))
