filename = 'pcc/chapter_10/pi_million_digits.txt'

def get_data(filename):
	with open(filename) as file_object:
		lines = file_object.readlines()
		data_string = ''
		for line in lines:
			data_string += line.strip()
		return data_string
		
pi_string = get_data(filename)

bdate = ''
err = False
while err == False:
	bdate = input("Enter Birthday (mmddyy) or q to quit: ")
	if bdate == 'q':
		break
	elif bdate in pi_string:
		print('True!')
	else:
		print('false!')		
print("Goodbye")



