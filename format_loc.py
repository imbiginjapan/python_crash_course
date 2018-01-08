from city_functions import format_location

print("enter 'q' to quit.")
while True:
	city = input("City? ")
	if city == 'q':
		break
	country = input("Country? ")
	if country == 'q':
		break
	population = input("Population? ")
	if population == 'q':
		break
	print(format_location(city,country,population))
