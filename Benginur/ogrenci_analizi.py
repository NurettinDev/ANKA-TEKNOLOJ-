# 1. DEĞİŞKEN ATAMA VE VERİ YAPILARI
GECME_NOTU = 50

# Öğrencilerin adlarını ve aldıkları notları içeren sözlük 
ogrenci_notlari = {
    "Ahmet Yılmaz": [45, 60, 55],
    "Ayşe Demir": [80, 90, 85],
    "Mehmet Kaya": [30, 40, 35],
    "Zeynep Çelik": [70, 75, 80],
    "Canan Şahin": [50, 55, 60]
}

# 2. FONKSİYONLAR
def ortalama_hesapla(not_listesi):
    """Bir öğrencinin aldığı notların ortalamasını hesaplar."""
    toplam = 0
    for not_degeri in not_listesi:  # FOR DÖNGÜSÜ
        toplam += not_degeri
    return toplam / len(not_listesi)

def harf_notu_donustur(ortalama):
    """Ortalamaya göre harf notu ataması yapar (Koşullu Yapılar)."""
    if ortalama >= 85:
        return "AA"
    elif ortalama >= 70:
        return "BA"
    elif ortalama >= 60:
        return "CB"
    elif ortalama >= GECME_NOTU:
        return "CC"
    else:
        return "FF"

def sistem_ozeti_goster(veri_sozlugu):
    """Tüm sınıfın analizini döngüler yardımıyla ekrana yazdırır."""
    print("=" * 45)
    print(f"{'ÖĞRENCİ ADI':<15} | {'ORTALAMA':<8} | {'DURUM':<6} | {'HARF'}")
    print("-" * 45)
    
    toplam_sinif_notu = 0
    ogrenci_sayisi = len(veri_sozlugu)
    
    
    for isim, notlar in veri_sozlugu.items():
        ortalama = ortalama_hesapla(notlar)  # Fonksiyon çağrısı
        harf = harf_notu_donustur(ortalama)    # Fonksiyon çağrısı
        
        toplam_sinif_notu += ortalama
        
        # Durum belirleme
        if ortalama >= GECME_NOTU:
            durum = "Geçti"
        else:
            durum = "Kaldı"
            
        print(f"{isim:<15} | {ortalama:<8.1f} | {durum:<6} | {harf}")
        
    print("-" * 45)
    sinif_ortalamasi = toplam_sinif_notu / ogrenci_sayisi
    print(f"Sınıf Geneli Ortalaması: {sinif_ortalamasi:.2f}")
    print("=" * 45)

# 3. WHILE DÖNGÜSÜ KULLANIMI
def ana_menu():
    """Kullanıcının sistemle etkileşime geçmesini sağlayan döngü yapısı."""
    while True:
        print("\n--- ÖĞRENCİ ANALİZ SİSTEMİ ---")
        print("1. Sınıf Raporunu Göster")
        print("2. Yeni Öğrenci Ekle")
        print("3. Çıkış Yap")
        
        secim = input("Lütfen bir işlem seçiniz (1-3): ")
        
        if secim == "1":
            sistem_ozeti_goster(ogrenci_notlari)
        elif secim == "2":
            yeni_isim = input("Öğrencinin Adı Soyadı: ")
            try:
                vize = float(input("Vize Notu: "))
                final = float(input("Final Notu: "))
                but = float(input("Bütünleme Notu: "))
                ogrenci_notlari[yeni_isim] = [vize, final, but]
                print(f"Başarıyla eklendi: {yeni_isim}")
            except ValueError:
                print("Hata: Lütfen geçerli bir sayı giriniz!")
        elif secim == "3":
            print("Sistemden çıkılıyor. İyi günler!")
            break  # WHILe DÖNGÜSÜNÜ SONLANDIRMA
        else:
            print("Geçersiz seçim! Lütfen 1, 2 veya 3 tuşlayın.")

# Programın Başlatılması
if __name__ == "__main__":
    ana_menu()
