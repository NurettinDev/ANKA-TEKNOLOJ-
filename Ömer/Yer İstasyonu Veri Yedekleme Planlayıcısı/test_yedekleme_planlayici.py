"""Görevdeki dört zorunlu durum ve sonraki tur için ek kontroller."""

import unittest

from yedekleme_planlayici import YedeklemePlanlayici, YedeklemeTalebi


def kimlikler(rapor, grup):
    return [kimlik for kimlik, _ in rapor[grup]]


class YedeklemePlanlayiciTestleri(unittest.TestCase):
    def test_kontrol_ornegi_ve_sonraki_tur(self):
        p = YedeklemePlanlayici()
        for talep in (
            YedeklemeTalebi("D1", 5, 6, "sağlam"),
            YedeklemeTalebi("D2", 4, 4, "sağlam"),
            YedeklemeTalebi("D3", 3, 3, "sağlam"),
            YedeklemeTalebi("D4", 2, 2, "bozuk"),
        ):
            p.talep_ekle(talep)

        ilk = p.tur_calistir(9)
        self.assertEqual(kimlikler(ilk, "kabul_edilenler"), ["D1", "D3"])
        self.assertEqual(kimlikler(ilk, "bekleyenler"), ["D2"])
        self.assertEqual(kimlikler(ilk, "reddedilenler"), ["D4"])
        self.assertEqual((ilk["kullanilan"], ilk["kalan"]), (9, 0))

        ikinci = p.tur_calistir(5)
        self.assertEqual(kimlikler(ikinci, "kabul_edilenler"), ["D2"])
        self.assertEqual(kimlikler(ikinci, "bekleyenler"), [])
        self.assertEqual(kimlikler(ikinci, "reddedilenler"), [])
        self.assertEqual((ikinci["kullanilan"], ikinci["kalan"]), (4, 1))

    def test_hepsi_saglam_ve_alan_yeterli(self):
        p = YedeklemePlanlayici()
        for kimlik, oncelik, alan in (("T1", 2, 5), ("T2", 5, 7), ("T3", 3, 6)):
            p.talep_ekle(YedeklemeTalebi(kimlik, oncelik, alan, "sağlam"))

        sonuc = p.tur_calistir(20)
        self.assertEqual(kimlikler(sonuc, "kabul_edilenler"), ["T2", "T3", "T1"])
        self.assertEqual(kimlikler(sonuc, "bekleyenler"), [])
        self.assertEqual(kimlikler(sonuc, "reddedilenler"), [])
        self.assertEqual((sonuc["kullanilan"], sonuc["kalan"]), (18, 2))

    def test_esit_oncelikte_eklenme_sirasi(self):
        p = YedeklemePlanlayici()
        for kimlik in ("E1", "E2", "E3"):
            p.talep_ekle(YedeklemeTalebi(kimlik, 4, 4, "sağlam"))
        p.talep_ekle(YedeklemeTalebi("E4", 5, 2, "sağlam"))

        sonuc = p.tur_calistir(10)
        self.assertEqual(kimlikler(sonuc, "kabul_edilenler"), ["E4", "E1", "E2"])
        self.assertEqual(kimlikler(sonuc, "bekleyenler"), ["E3"])
        self.assertEqual((sonuc["kullanilan"], sonuc["kalan"]), (10, 0))

    def test_buyuk_dosya_beklerken_kucuk_dosya_sigar(self):
        p = YedeklemePlanlayici()
        for kimlik, oncelik, alan in (
            ("K1", 5, 6), ("K2", 4, 7), ("K3", 3, 3), ("K4", 2, 1)
        ):
            p.talep_ekle(YedeklemeTalebi(kimlik, oncelik, alan, "sağlam"))

        sonuc = p.tur_calistir(10)
        self.assertEqual(kimlikler(sonuc, "kabul_edilenler"), ["K1", "K3", "K4"])
        self.assertEqual(kimlikler(sonuc, "bekleyenler"), ["K2"])
        self.assertEqual((sonuc["kullanilan"], sonuc["kalan"]), (10, 0))

    def test_bozuk_ve_gecersiz_kayitlar_reddedilir(self):
        p = YedeklemePlanlayici()
        for talep in (
            YedeklemeTalebi("G1", 5, 5, "bozuk"),
            YedeklemeTalebi("G2", 4, 0, "sağlam"),
            YedeklemeTalebi("G3", 6, 3, "sağlam"),
            YedeklemeTalebi("G4", 4, 4, "sağlam"),
            YedeklemeTalebi("G4", 5, 2, "sağlam"),
            YedeklemeTalebi("", 3, 2, "sağlam"),
            YedeklemeTalebi("G5", True, 2, "sağlam"),
        ):
            p.talep_ekle(talep)

        sonuc = p.tur_calistir(15)
        self.assertEqual(kimlikler(sonuc, "kabul_edilenler"), ["G4"])
        self.assertEqual(kimlikler(sonuc, "bekleyenler"), [])
        self.assertEqual(
            kimlikler(sonuc, "reddedilenler"),
            ["G1", "G2", "G3", "G4", "", "G5"],
        )
        self.assertEqual((sonuc["kullanilan"], sonuc["kalan"]), (4, 11))

    def test_eski_bekleyen_yeni_esit_oncelikliden_once(self):
        p = YedeklemePlanlayici()
        p.talep_ekle(YedeklemeTalebi("A", 4, 4, "sağlam"))
        p.talep_ekle(YedeklemeTalebi("B", 4, 4, "sağlam"))
        ilk = p.tur_calistir(4)
        self.assertEqual(kimlikler(ilk, "bekleyenler"), ["B"])

        p.talep_ekle(YedeklemeTalebi("C", 4, 4, "sağlam"))
        ikinci = p.tur_calistir(4)
        self.assertEqual(kimlikler(ikinci, "kabul_edilenler"), ["B"])
        self.assertEqual(kimlikler(ikinci, "bekleyenler"), ["C"])

    def test_gecersiz_tur_kapasitesi(self):
        p = YedeklemePlanlayici()
        with self.assertRaises(ValueError):
            p.tur_calistir(-1)
        with self.assertRaises(ValueError):
            p.tur_calistir(True)


if __name__ == "__main__":
    unittest.main()
