class ChargingStation:
    
    def __init__(self, cs_capacity_input , batteries, max_temp = 45, min_temp = 0):
        self.cs_capacity = cs_capacity_input
        self.all_batteries = batteries
        self.max_temp = max_temp 
        self.min_temp = min_temp
        self.cs_situation()
        
    def cs_situation(self):
        print("ŞARJ İSTASYONU".center(30, "-"))
        print(f"Şarj İstasyonu Kapasitesi : {self.cs_capacity}\nŞarj istasyonunda {len(self.all_batteries)} tane batarya var")

        for battery_id, battery in self.all_batteries.items():
            print(f"{battery_id} ID'li batarya için :\n\tŞarj İstasyonundan İstenilen Enerji : {battery.energy_needed}" 
                  f"\n\tBataryanın Sıcaklığı : {battery.battery_temp}"
                  f"\n\tBatarya Önceliği : {battery.priority}")
