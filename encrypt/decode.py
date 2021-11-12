from caesar.decrypt import caesar_decrypt
def decode(data,key):
	key_progress = 0
	unencrypted_data = ""
	for a in data:
		unencrypted_data = unencrypted_data + caesar_decrypt(a,int(key[key_progress]))
		key_progress = key_progress + 1
	return unencrypted_data