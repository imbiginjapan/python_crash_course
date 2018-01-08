from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
	""" Return the pygal 2 latter country code for the given country. """
	
	for code,name in COUNTRIES.items():
		if name == country_name:
			return code
	# Return None if country code not found.
	return None


