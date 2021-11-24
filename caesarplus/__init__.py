# caesarplus Main Module
# Owner: awesomelewis2007
# Co-Owner: WolfieBoy


COMMANDS = [
	"encode",
	"decode"
]
from .encrypt import caesar_encrypt
from .decrypt import caesar_decrypt
import random
def encode(data):
	key = []
	encrypted_data = ""
	for a in data:
		key.append(random.randint(0,9))
		encrypted_data = encrypted_data + caesar_encrypt(a,key[-1])
	return key,encrypted_data
def decode(key,data):
	key_progress = 0
	unencrypted_data = ""
	for a in data:
		unencrypted_data = unencrypted_data + caesar_decrypt(a,int(key[key_progress]))
		key_progress = key_progress + 1
	return unencrypted_data