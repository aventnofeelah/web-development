from models import Vehicle, Car, Motorcycle

vehicle1 = Vehicle("Generic", "Transport", 2000)
car1 = Car("Dodge", "Challenger", 2026, 2)
moto1 = Motorcycle("Yamaha", "R1", 2021, False)

vehicles = [vehicle1, car1, moto1]

for v in vehicles:
    print(v)
    print(v.start_engine())
    print(v.move())
    print()

print(car1.honk())
print(moto1.wheelie())