import json
import pygal
from pygal.style import LightColorizedStyle, RotateStyle
from country_codes import get_country_code

# load the data into a list.
filename = '/media/jeremy/ExtraDrive1/python_cc/pcc/chapter_16/population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

# Build a dictionary of population Data
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if not code:
			print(country_name)
			
			
