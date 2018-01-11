
user_list = []

def add_user(user):

	"""
	Agrega un usuario a la lista

	>>> user_list = []
	... add_user('a')	
	user_list = ['a']
	>>>
	"""

	user_list.append(user)

def mod_user(item_find, item_replace):

	"""
	Modifica el item_find por el item_replace en una lista

	>>> user_list = ['a','b']
	... mod_user('a','c')	
	user_list = ['c','b']
	>>>	
	"""

	
	if item_find in user_list:
		x = user_list.index(item_find)
		user_list[x] = item_replace
	
	else:
		return "User not found"	


def remove_user(user):

	"""
	Borra de la lista el usuario

	>>> user_list = ['a','b']
	... remove_user('a')	
	user_list = [b']
	>>>	

	"""
	
	if user in user_list:
		user_list.remove(user)

	else:	
		return "User not found"	





if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

