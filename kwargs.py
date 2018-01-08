

def make_car(make,model,**attrs):
	cars = {}
	cars['make'] = make
	cars['model'] = model
	for k,v in attrs.items():
		cars[k] = v
	return cars
	
car = make_car('toyota','previa',rhd = True,
				color = 'Blue',tire_size = 15)
print(car)
