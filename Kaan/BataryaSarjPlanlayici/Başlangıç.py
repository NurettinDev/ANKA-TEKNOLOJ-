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
        print(f"{self.battery_id} ID'li BATARYA".center(70, "-"))
        request_dict = dict()
        request_features = ["İstenilen Enerji","Sıcaklık"]
        request_dict["ID"] = self.battery_id 

        for feature in request_features:
            feature_val = check_input(f"{self.battery_id} ID'li batarya için {feature} değerini giriniz : ")
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
        print("\nŞARJ İSTASYONU".center(30, "-"))
        print("-" * 35 + f"\nŞarj İstasyonu Kapasitesi : {self.cs_capacity}\nŞarj istasyonunda {len(self.all_batteries)} tane batarya var")

        for battery_id, battery in self.all_batteries.items():
            print(f"{battery_id} ID'li batarya için :\n\tŞarj İstasyonundan İstenilen Enerji : {battery.energy_needed} \n\tBataryanın Sıcaklığı : {battery.battery_temp}")

class BatteryChargingProcess:
    
    def __init__(self, charging_station_inp):
        self.charging_station = charging_station_inp
        self.batteries = self.charging_station.all_batteries
        self.in_process = list(self.batteries.keys())
        self.total_cap_used = 0
        self.cs_isFull = False
        self.accepted, self.refused, self.waiting = [], [], []

    def checkTemp(self):
        print("\nSICAKLIK KONTROL".center(30, "-"))

        for battery_id, battery in self.batteries.items(): # batarya enerji isteği şarj istasyonunun kapasitesini geçmesi bir sorun değildir
            if battery.battery_temp > self.charging_station.max_temp or battery.battery_temp < self.charging_station.min_temp:
                self.refused.append(battery_id)
                self.in_process.remove(battery_id)
                print(f"Sıcaklık sınır dışına çıktığından dolayı {battery_id} ID'li bataryanın şarj isteği reddedildi")
            else:
                print(f"{battery_id} ID'li batarya sıcaklık kontrolünden geçti")   

    def putInOrder(self):
        # zaten id ler sıralı geliyor 
        # ilk bataryayı kabul et diğerlerini dolaş her biri için enerji toplamı istasyon kapasitesini geçiyorsa waite al
        # geçmiyorsa accepted durumuna al ve kullanılan toplam kapasiteyi güncelle

        for battery_id in self.in_process:
            battery = self.batteries[battery_id]
            if self.total_cap_used + battery.energy_needed <= self.charging_station.cs_capacity:
                self.accepted.append(battery_id)
                self.total_cap_used += battery.energy_needed
            else:
                self.waiting.append(battery_id)
                print(f"{battery_id} ID'li batarya yetersiz kapasiteden dolayı bekleyenler listesine alındı")

        print("\nSONUC".center(30, "-"))
        print(f"Kabul Edilen Batarya ID'leri (Şarj Sırasına Uygun) : {self.accepted}\nBekleyen Batarya ID'leri : {self.waiting}\nReddedilen Batarya ID'leri : {self.refused}")
        print(f"Batarya Kapasitesi : {self.charging_station.cs_capacity}\nKullanılan İstasyon Kapasitesi : {self.total_cap_used}\nKalan İstasyon Kapasitesi : {self.charging_station.cs_capacity - self.total_cap_used}")

def check_input(prompt):
    while True:
        try:
            return int(input(prompt)) # bir daha input isteniyor sonsuz döngüye girmez
        except ValueError:
            print("Yanlış değer girildi lütfen tekrar giriniz.")

battery_amount = check_input("Batarya sayısını giriniz : ")
batteries = dict()

for i in range(battery_amount):
    battery= Battery()
    battery.create_battery()  
    batteries[battery.battery_id] = battery

station = ChargingStation(10,batteries)
station.cs_situation()

process = BatteryChargingProcess(station)
process.checkTemp()
process.putInOrder()