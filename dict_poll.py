langs = {
		 'jen': 'python',
		 'sarah': 'c',
		 'edward': 'ruby',
		 'phil': 'python',
		 }
poll = ['jen','bob','edward','phil','chris']
for name in poll:
	if name in langs.keys():
		print("ok")
	else:
		print("not ok")
