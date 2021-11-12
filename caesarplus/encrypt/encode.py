from caesar.encrypt import caesar_encrypt
import random
def encode(data):
	key = []
	encrypted_data = ""
	for a in data:
		key.append(random.randint(0,9))
		encrypted_data = encrypted_data + caesar_encrypt(a,key[-1])
	return key,encrypted_data