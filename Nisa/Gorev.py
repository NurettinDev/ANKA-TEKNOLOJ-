class Bakim_isi:
    def __init__(self,Kimlik,Oncelik,Sure,Ekipman_hazir):  
        self.Kimlik = Kimlik
        self.Oncelik= Oncelik
        self.Sure= Sure
        self.Ekipman_hazir= Ekipman_hazir
        self.Ret_nedeni=""
        self.Bekleme_nedeni=""
    def __str__(self):
        return f"Kimlik: {self.Kimlik}, Öncelik: {self.Oncelik}, Süre: {self.Sure}, Ekipman: {self.Ekipman_hazir}" 
        #Nesnenin kullanıcı tarafından kolay okunmasını sağlıyoruz ve çıktıyı daha kolay çıkartıyoruz.

class Bakim_Planlayicisi:
    def __init__(self,Kapasite):
        self.Kapasite= Kapasite
        self.Kalan_Sure = Kapasite
        self.Kabul_edilenler = []
        self.Bekleyenler = []
        self.Reddedilenler = []

    def Plan_yap(self, isler):
     for bakim in isler:
      if not isinstance(bakim.Sure,int) or bakim.Sure <= 0:
        bakim.Ret_nedeni="Süre pozitif tam sayı değil."        #Süre pozitif ya da tam sayı değilse reddeder.
        self.Reddedilenler.append(bakim)
         
      elif bakim.Ekipman_hazir == False:     #Bakım işinin onaylanması,reddedilmesi,bekletilmesi
        bakim.Ret_nedeni="Ekipman hazır değil."
        self.Reddedilenler.append(bakim)

      elif self.Kalan_Sure >= bakim.Sure: 
           self.Kabul_edilenler.append(bakim)
           self.Kalan_Sure -= bakim.Sure
  
      else: 
        self.Bekleyenler.append(bakim)
        bakim.Bekleme_nedeni="Süre kalan kapasiteye sığmadı."
       

Bakim_isi1_obj = Bakim_isi("M1", 3 , 2 ,  True  )
Bakim_isi2_obj = Bakim_isi("M2", 2 , 3.5 , True )
Bakim_isi3_obj = Bakim_isi("M3", 5 , 2 ,  True  )
Bakim_isi4_obj = Bakim_isi("M4", 1 ,-5 ,  True  )

Isler = [Bakim_isi1_obj,Bakim_isi2_obj,Bakim_isi3_obj,Bakim_isi4_obj] #Kimlikleri listenin içine koyuluyor.


def Oncelik_al(Sira):
    return Sira.Oncelik

Isler.sort(key=Oncelik_al , reverse= True)  #Büyükten küçüğe önceliğe göre sıralama


Planlayici_obj= Bakim_Planlayicisi(13) #Kapasite ayarlama ve "Bakım_Planlayicisi" sınıfını çağırma
Planlayici_obj.Plan_yap(Isler)   

for Bakim in Isler: #Özellikleri çıktı alma
    print(Bakim)

#kapasite,kalansüre, kabul edilme,reddedilme,bekleme durumunu çıktı alma

print("Kapasite=", Planlayici_obj.Kapasite)

print("Kalan Süre=", Planlayici_obj.Kalan_Sure)

print("Kabul edilenler=")
for bakim in Planlayici_obj.Kabul_edilenler:
   print(bakim)

print("Reddedilenler=")
for bakim in Planlayici_obj.Reddedilenler:
    print(bakim.Kimlik,"reddedildi: ", bakim.Ret_nedeni)

print("Bekleyenler=")
for bakim in Planlayici_obj.Bekleyenler:
    print(bakim.Kimlik, "bekliyor: ", bakim.Bekleme_nedeni)








