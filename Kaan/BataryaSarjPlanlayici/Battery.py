from Functions import check_input

class Battery:
    battery_count = 0

    def __init__(self):
        self.battery_id = Battery.battery_count
        Battery.battery_count += 1
        self.battery_temp = None
        self.energy_needed = None
        self.priority = None
        self.create_battery()
        
    def __repr__(self):
        return(f"\nid : {self.battery_id} battery_temp : {self.battery_temp} energy_needed : {self.energy_needed}" 
            "\n-------------------------------------------------------------")   
        
    def create_battery(self): # sonradan eklenebilecek özelliklere karşın
        print(f"{self.battery_id} ID'li BATARYA".center(70, "-"))
        request_dict = dict()
        request_dict["ID"] = self.battery_id 

        self.energy_needed = check_input("İstenilen Enerji : ", minval=1)
        self.battery_temp = check_input("Sıcaklık : ")                     
        self.priority = check_input("Öncelik (1-5) : ", 1, 5)