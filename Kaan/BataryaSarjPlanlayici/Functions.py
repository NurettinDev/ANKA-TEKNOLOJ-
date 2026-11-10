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