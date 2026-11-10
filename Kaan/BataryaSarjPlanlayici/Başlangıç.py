# Sıcaklık ve talep önceliğ, kapasite, kimlik
# Talep oluşturmak için ayrı bir yapı bulunmalı talepte : 
#   Batarya kimliği, 
#   öncelik (1-5), (EN ÖNEMLİSİ SICAKLIK SONRA KAYIT ZAMANI BU BİLGİLER İLE ÖEM SIRASI OLUŞTURULMALI)
#   istenen enerji (pozitif tam sayı, birim), 
#   sıcaklık (sayı, °C).

batteries = dict()

class Battery:
    battery_count = 0

    def __init__(self):
        self.battery_id = Battery.battery_count
        Battery.battery_count += 1
        self.battery_temp = None
        self.energy_needed = None

    def __repr__(self):
        return(f"\nid : {self.battery_id} battery_temp : {self.battery_temp} energy_needed : {self.energy_needed}" 
            "\n-------------------------------------------------------------")   
        
    def create_battery(self): # sonradan eklenebilecek özelliklere karşın
        print(f"{self.battery_id} ID'li BATARYA ÖZELLİKLERİ".center(90, "-"))
        request_dict = dict()
        request_features = ["İstenilen Enerji","Sıcaklık"]
        request_dict["ID"] = self.battery_id 

        for feature in request_features:
            feature_val = int(input(f"{self.battery_id} ID'li batarya için {feature} değerini giriniz : "))
            request_dict[feature] = feature_val

        self.battery_temp = request_dict["Sıcaklık"]
        self.energy_needed = request_dict["İstenilen Enerji"]

class ChargingStation:
    
    def __init__(self, cs_capacity_input , batteries, max_temp = 45, min_temp = 0):
        self.cs_capacity = cs_capacity_input
        self.all_batteries = batteries
        self.max_temp = max_temp 
        self.min_temp = min_temp

    def cs_situation(self):
        print("ŞARJ İSTASYONU".center(90, "-"))
        print("-" * 35 + f"\nŞarj İstasyonu Kapasitesi : {self.cs_capacity}\nŞarj istasyonunda {len(self.all_batteries)} tane batarya var")

        for battery_id, battery in self.all_batteries.items():
            print(f"{battery_id} ID'li batarya için :\n\tŞarj İstasyonundan İstenilen Enerji : {battery.energy_needed} \n\tBataryanın Sıcaklığı : {battery.battery_temp}")

class BatteryChargingProcess:

    def __init__(self, charging_station):
        self.charging_station = charging_station
        self.batteries = charging_station.all_batteries
        self.in_process = list(self.batteries.keys())
        self.accepted, self.refused, self.waiting = [], [], []

    def checkTemp(self):
        print("SICAKLIK KONTROL".center(90, "-"))

        for battery_id, battery in self.batteries.items(): # batarya enerji isteği şarj istasyonunun kapasitesini geçmesi bir sorun değildir
            if battery.battery_temp >= self.charging_station.max_temp or battery.battery_temp <= self.charging_station.min_temp:
                self.refused.append(battery_id)
                self.in_process.pop(battery_id)
                print(f"Sıcaklık sınır dışına çıktığından dolayı {battery_id} ID'li bataryanın şarj isteği reddedildi")
            else:
                print(f"{battery_id} ID'li batarya sıcaklık kontrolünden geçti")   

    def putInOrder(self):
        # zaten id ler sıralı geliyor 
        # ilk bataryayı kabul et diğerlerini dolaş her biri için enerji toplamı istasyon kapasitesini geçiyorsa awaite al geçmiyorsa accepted durumuna al
        # hatta bataryanın şarj durumlarını sürekli kontrol ederek bir bataryanın tamamının şarj olmasını beklemeden diğer sıradakini şarja al 
        ...
            



battery_amount = int(input("Batarya sayısını giriniz : "))

for i in range(battery_amount):
    battery= Battery()
    battery.create_battery()  
    batteries[battery.battery_id] = battery

station = ChargingStation(100,batteries)
station.cs_situation()

process = BatteryChargingProcess(batteries)
process.checkTemp()