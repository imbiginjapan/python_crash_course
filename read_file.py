filename = 'pcc/chapter_10/programming.txt'

''' read entire object as a file object '''
with open(filename) as file_object:		
	lines = file_object.read()
	print(lines.rstrip())
print('')

''' read line by line as a file object '''
with open(filename) as file_object:		
	for line in file_object:
		print(line.rstrip())
print('')
		
''' copy then read out of list '''
with open(filename) as file_object:			
	lines = file_object.readlines()
	for line in lines:
		print(line.rstrip())
print('')
	
  


