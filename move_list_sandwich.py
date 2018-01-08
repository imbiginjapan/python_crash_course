sandwich_orders = ["pastrami","tuna","ham","pastrami","pastrami","roast beef"]
finished_sandwiches = []

def out_of(ingredient,sandwich_orders):
	while ingredient in sandwich_orders:
		sandwich_orders.remove(ingredient)
	
	return sandwich_orders


print("Out of pastrami!")
out_of('pastrami',sandwich_orders)	
while sandwich_orders:
	work_on = sandwich_orders.pop()
	
	print("I made a " + work_on + " sandwich")
	finished_sandwiches.append(work_on)
	
print(finished_sandwiches)
