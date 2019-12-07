import math

mass = []
total = 0

with open('d1.txt') as f:
	for line in f:
		data = line.strip()
		mass.append(int(data))

print(mass)

for component in mass:
	fuel = math.floor(component/3)-2
	total = total + fuel
	while fuel > 0:
		fuel = math.floor(fuel/3)-2
		print(fuel)
		if not fuel<0:
			total = total+fuel

print(total)
