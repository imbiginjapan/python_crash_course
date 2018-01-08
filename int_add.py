while True:
	num_1 = input("Number 1? (or 'q' to quit) ")
	if num_1 == 'q':
		break
	num_2 = input("Number 2? (or 'q' to quit) ")
	if num_2 == 'q':
		break
	try:
		total = float(num_1) + float(num_2)
	except ValueError:
		print("Please enter numbers only")
	else:
		print("Total: " + str(total))
