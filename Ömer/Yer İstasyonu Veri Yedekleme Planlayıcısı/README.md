# Yer İstasyonu Veri Yedekleme Planlayıcısı

Bu program gerçek dosyaları kopyalamaz. Yer istasyonundaki dosyalar için
tanımlanan yedekleme taleplerinin hangi turda seçileceğini simüle eder.
`yedekleme_planlayici.py` iki sınıf içerir: `YedeklemeTalebi` tek talebin
bilgilerini, `YedeklemePlanlayici` ise kapasiteyi ve kararları yönetir.

## Çalıştırma

Bu klasörde aşağıdaki komutları çalıştırın:

```powershell
python yedekleme_planlayici.py
python -m unittest -v test_yedekleme_planlayici.py
```

İlk komut görev metnindeki 9 MB örneğini ve isteğe bağlı ikinci turu gösterir.
İkinci komut yedi otomatik testi çalıştırır. Harici kütüphane gerekmez.

## Algoritma açıklaması

1. Her talebi benzersiz kimlik, öncelik, gerekli alan ve sağlamlık bilgisiyle kaydederim.
2. Boş veya tekrar eden kimliği, 1-5 dışındaki önceliği ve pozitif tam sayı olmayan alanı reddederim.
3. Bozuk dosyayı da nedeniyle reddederim; reddedilen talep kapasite kullanmaz.
4. Kalan sağlam talepleri yüksek öncelikten düşüğe sıralarım.
5. Öncelikler eşitse sisteme önce eklenen talebi önce değerlendiririm.
6. Talep kalan alana sığarsa kabul edip alanını tur kotasından düşerim.
7. Sığmayanı beklemeye alır, sonraki daha küçük talepleri de kontrol ederim.
8. Tur sonunda kararları, nedenleri, kullanılan ve kalan alanı raporlarım.
9. İsteğe bağlı sonraki turda yalnızca bekleyen talepleri yeni kotayla yeniden denerim.

## Test durumları ve sonuçları

| Durum | Beklenen sonuç | Gerçek sonuç |
| --- | --- | --- |
| Görevdeki 9 MB örneği | D1 ve D3 kabul, D2 bekler, D4 reddedilir; 9 MB kullanılır | Eşleşti |
| Tüm dosyalar sağlam, alan yeterli | T2, T3, T1 kabul; 18 MB kullanılır, 2 MB kalır | Eşleşti |
| Eşit öncelik | E4, E1, E2 kabul; E3 bekler | Eşleşti |
| Büyük dosya sığmaz, küçükler sığar | K1, K3, K4 kabul; K2 bekler | Eşleşti |
| Bozuk veya geçersiz kayıtlar | Yalnız geçerli G4 kabul; diğerleri nedenleriyle reddedilir | Eşleşti |
| Sonraki tur | D2, yeni 5 MB kotada kabul edilir; 1 MB kalır | Eşleşti |
| Eski bekleyen ve yeni eşit öncelikli talep | Eski B, yeni C'den önce değerlendirilir | Eşleşti |

Test komutunun sonucu: `Ran 7 tests` ve `OK`.

## Kapsam notu

Görev metni tek turluk planlama istiyor. Bekleyen talebin sonraki tura
aktarılması ek bir simülasyon özelliğidir. Her turda verilen kapasite yeni bir
tur kotasıdır; program fiziksel diskin toplam boş alanını takip etmez.
