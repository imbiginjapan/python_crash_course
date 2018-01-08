active = True
while active:
	topping = input("Enter topping or 'quit': ")
	if topping == "quit":
		active = False
	else:
		print("Adding " + topping)
