def format_location(city,country,population = ''):	
	if population:
		location = city + ", " + country + " Population " + population
	else:
		location = city + ", " + country
	return location.title()
		
