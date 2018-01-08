
with open("listfile.txt","a") as file_object:
	exit_loop = False
	
	while exit_loop == False:
		text_string = input("Line? (or 'q' to quit): ")
		if text_string == 'q':
			exit_loop = True
		else:
			file_object.write(text_string + '\n')
