class BatteryChargingProcess:
    
    def __init__(self, charging_station_inp):
        self.charging_station = charging_station_inp
        self.batteries = self.charging_station.all_batteries
        self.total_cap_used = 0
        self.in_process, self.accepted, self.refused, self.waiting, self.orderedid = dict(), [], [], [], []

    def run(self):
        self.create_prioritised()
        self.checkTemp()
        self.putInOrder()

    def create_prioritised(self):
            for id, b in self.batteries.items():
                self.in_process[id] = b.priority  

    def checkTemp(self):
        print("SICAKLIK KONTROL".center(30, "-"))

        for battery_id, battery in self.batteries.items(): 
            if battery.battery_temp > self.charging_station.max_temp or battery.battery_temp < self.charging_station.min_temp:
                self.refused.append(battery_id)
                del self.in_process[battery_id]
                print(f"Sıcaklık sınır dışına çıktığından dolayı {battery_id} ID'li bataryanın şarj isteği reddedildi")
            else:
                print(f"{battery_id} ID'li batarya sıcaklık kontrolünden geçti")   

    def putInOrder(self):
        # ilk bataryayı kabul et diğerlerini dolaş her biri için enerji toplamı istasyon kapasitesini geçiyorsa waite al
        # geçmiyorsa accepted durumuna al ve kullanılan toplam kapasiteyi güncelle        
        
        # id lere karşılık gelen öncelikler dict e alındı şimdi öncelikler büyükten küçüğe sıralanmalı
        self.orderedid = sorted(self.in_process.keys(), key=self.in_process.get, reverse=True) 
        # her id için get çalıştırır. get key in valuesunu döndürür , get parantezsiz olacak direkt fonksiyonun kendisini vericez
        # get kullanmayabilirdik de. in process in keylerine priority valuelarına id verebilirdik
        print("Önem sırasına göre sıralanmış işlenecek liste oluşturuldu.")
        print(f"Oluşan Lİste : {self.in_process}")

        for battery_id in self.orderedid:
            battery = self.batteries[battery_id]

            if self.total_cap_used + battery.energy_needed <= self.charging_station.cs_capacity:
                self.accepted.append(battery_id)
                self.total_cap_used += battery.energy_needed
            else:
                self.waiting.append(battery_id)
                print(f"{battery_id} ID'li batarya yetersiz kapasiteden dolayı bekleyenler listesine alındı")

        print("SONUC".center(30, "-"))
        print(f"Kabul Edilen Batarya ID'leri (Şarj Sırasına Uygun) : {self.accepted}\nBekleyen Batarya ID'leri : {self.waiting}\nReddedilen Batarya ID'leri : {self.refused}")
        print(f"Batarya Kapasitesi : {self.charging_station.cs_capacity}\nKullanılan İstasyon Kapasitesi : {self.total_cap_used}\nKalan İstasyon Kapasitesi : {self.charging_station.cs_capacity - self.total_cap_used}")

def check_input(prompt, minval = None, maxval= None):
    while True:
        try:
            val = int(input(prompt))
        except ValueError:
            print("Lütfen bir tam sayı giriniz.")
            continue
        if minval is not None and val < minval:
            print(f"Değer en az {minval} olmalıdır.")
        elif maxval is not None and val > maxval:
            print(f"Değer en çok {maxval} olmalıdır.")
        else:
            return val