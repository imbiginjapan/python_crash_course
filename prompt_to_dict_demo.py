responses = {}

poll_active = True

while poll_active:
	name = input("Name? ")
	response = input("Hobby? ")
	
	responses[name] = response
	
	repeat = input("More y/n? ")
	
	if repeat == 'n':
		poll_active = False
		
print("\nResults: ")
for name, response in responses.items():
	print(name + ":" + response)
