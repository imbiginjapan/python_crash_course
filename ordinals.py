nums = range(1,10)
for num in nums:
	if num > 3:
		print(str(num) + "th")
	elif num == 2:
		print(str(num) + "nd")
	elif num == 3:
		print(str(num) + "rd")
	else:
		print(str(num) + "st")
