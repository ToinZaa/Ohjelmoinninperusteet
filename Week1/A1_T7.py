print("Calculate fuel consumption.")
# Syötetään matka ja polttoaineen kulutus
Feed = input("Enter travel distance(kilometers): ")
Distance = int(Feed)
Feed = input("Enter fuel usage(liters): ")
# Lasketaan kulutus
FuelUsage = int(Feed)
Consumption = (FuelUsage / Distance) * 100
Consumption = int(Consumption)
# int muuttaa desimaaliluvun kokonaisluvuksi
print("Fuel consumption is", Consumption, "l per 100 km")
