# Sıcaklık ve talep önceliğ, kapasite, kimlik
# Talep oluşturmak için ayrı bir yapı bulunmalı talepte : 
#   Batarya kimliği, 
#   öncelik (1-5), (EN ÖNEMLİSİ SICAKLIK SONRA KAYIT ZAMANI BU BİLGİLER İLE ÖEM SIRASI OLUŞTURULMALI)
#   istenen enerji (pozitif tam sayı, birim), 
#   sıcaklık (sayı, °C).

max_temp = 45
min_temp = 0
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
        request_dict = dict()
        request_features = ["İstenilen Enerji","Sıcaklık"]

        for feature in request_features:
            feature_val = int(input(f"{self.battery_id} ID'li batarya için {feature} değerini giriniz : "))
            request_dict[feature] = feature_val

        self.battery_temp = request_dict["Sıcaklık"]
        self.energy_needed = request_dict["İstenilen Enerji"]        
        return request_dict


for i in range(2):
    battery= Battery()
    battery.create_battery()  
    batteries[battery.battery_id] = battery

for id, battery_features in batteries.items():
    print(id, battery_features)