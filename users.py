import user_ctrl
users = []
users.append(user_ctrl.User("Bob","Smith"))
users.append(user_ctrl.User("Emma","Reed"))
users.append(user_ctrl.Admin("Al","Jolson"))


for user in users:
	user.greet_user()
	user.privileges.show_privileges()
