import json


def get_stored_user(filename):
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
	
		
def get_new_user(filename):
	username = input("What is your name?")
	
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
	
	print("Hello, " + username + ".")
	return username
	
	
def greet_user(filename):
	username = get_stored_user(filename)
	
	if username:
		response = validate_user(username)		
		if response == 'y':
			print("Welcome back " + username + "!")
		else:
			username = get_new_user(filename)
	else: 
		username = get_new_user(filename)
		
	
		
def validate_user(username):
	valid = False
	while not valid:
		response = input("Are you " + username + "? (y/n)").lower()
	
		if response not in ['y','n']:
			 print("Please enter 'y' or 'n'")
		else:
			valid = True
	
	return response


filename = 'user_login.json'
greet_user(filename)
