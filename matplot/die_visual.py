import pygal

from die import Die

dice = [Die(),Die(),Die()]


results = [] 
for num in range (1000):
	result = 0
	for die_1 in dice:
		result += die_1.roll()
	results.append(result)
	
frequencies = []
max_result = len(dice) * dice[1].num_sides
for value in range(len(dice), max_result+1):
	print(results)
	frequency = results.count(value)
	frequencies.append(frequency)
	
hist = pygal.Bar()

hist.title = "Results of rolling %dd%d 1000 times" % (
				len(dice),dice[1].num_sides)
hist.x_labels = range(len(dice),max_result+1)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('Total' , frequencies)
hist.render_to_file('die_visual.svg')
