from Battery import Battery
from ChargingStation import ChargingStation
from Functions import check_input, BatteryChargingProcess
# kendim çağırdığım tüm metodları sınıflar içerisinde kendi kendine çağırttırsam daha iyi olur

battery_amount = check_input("Batarya sayısını giriniz : ") # bunlar da functionsa atılabilir
charging_capasity = check_input("Şarj kapasitesini giriniz : ")
batteries = dict()

for i in range(battery_amount):
    battery= Battery()
    batteries[battery.battery_id] = battery

station = ChargingStation(charging_capasity, batteries)
process = BatteryChargingProcess(station)
process.run()

