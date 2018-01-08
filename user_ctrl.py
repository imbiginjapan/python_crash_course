class User():

	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
		self.privileges = Privileges([True,False,False])
	
	def greet_user(self):
		print("Hello, " + self.describe_user())
		
	def describe_user(self):
		return self.first_name.title() + " " + self.last_name.title()
	
	def increment_login_attempt(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		
		
		
class Admin(User):
	
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = Privileges([True,True,True])


class Privileges():
	
	def __init__(self,params):
		self.privileges = {"can_add_post" : params[0],
						   "can_delete_post" : params[1],
						   "can_ban_user" : params[2]}
						   
	def show_privileges(self):
		print(self.privileges)
	
		
		
