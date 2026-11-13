    
def bilet_fiyati_hesapla(yas, ogrenci_mi, bilet_sayisi):

    birim_fiyat = 150.0
    
   
    if yas < 7:

        print("7 yaş altı giriş ücretsiz.")

        return 0.0
    
    # İndirim oranını belirleme 

    if ogrenci_mi or yas <= 18:
        indirim_orani = 0.30  

    elif yas >= 65:
        indirim_orani = 0.40  

    else:
        indirim_orani = 0.0
        
    indirimli_fiyat = birim_fiyat * (1 - indirim_orani)

    toplam_tutar = indirimli_fiyat * bilet_sayisi
    
    
    if bilet_sayisi >= 5 and indirim_orani < 0.50:

        toplam_tutar *= 0.90

        print("Toplu alım indirimi uygulandı!")
        
    return round(toplam_tutar, 2)


if __name__ == "__main__":

    yas = 20

    ogrenci = True

    adet = 3
    
    tutar = bilet_fiyati_hesapla(yas, ogrenci, adet)
    
    print(f"Ödenecek toplam tutar: {tutar} TL")