#operatör kullanım maliyeti
#4 dk dan az konuşmuşsa fix 50 tl alınır fazla konuşulursa her dk için +5 lira
minutes=int(input("Enter the call duration in minutes:"))

fixed_free=50
free_minutes=4
extra_free_per_minutes=5

if(minutes<=free_minutes):
    total_cost=fixed_free
else:
    extra_minutes=minutes-free_minutes
    total_cost=fixed_free+(extra_minutes*extra_free_per_minutes)
print(f"Total cost for a {minutes}- minute call: {total_cost} TL")
