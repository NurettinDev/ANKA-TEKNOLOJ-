from Functions import check_input

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