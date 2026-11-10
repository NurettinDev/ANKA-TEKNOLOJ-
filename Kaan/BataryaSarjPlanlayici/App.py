from Battery import Battery
from ChargingStation import ChargingStation
from Functions import check_input, BatteryChargingProcess

battery_amount = check_input("Batarya sayısını giriniz : ")
charging_capasity = check_input("Şarj kapasitesini giriniz : ")

batteries = dict()

for i in range(battery_amount):
    battery= Battery()
    battery.create_battery()  
    batteries[battery.battery_id] = battery

station = ChargingStation(charging_capasity, batteries)
station.cs_situation()

process = BatteryChargingProcess(station)
process.checkTemp()
process.putInOrder()