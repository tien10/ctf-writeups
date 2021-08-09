import itertools
import hashlib
import string

table = string.ascii_letters + string.digits + "._"
salts = ['pVOjnnmk','RGiledp6', 'Mvcezxls']
run = [b'\xbf\xf1\x26\xdc', b'\xb3\x07\x00\x00', b'\x00\xff\xd6\xc3']

ind = 0
for i in range(0, 3):		#3 remaining keys
	salt = salts[i]
	for v in itertools.product(table, repeat=4):
		msgDigest =  hashlib.md5((''.join(v) + salt).encode()).digest()
		if i ==0:					
			ind = 2				#specified pos of running code
		elif i == 1: 		
			ind = 7				#specified pos of running code
		else:
			ind = 1				#specified pos of running code
		if run[i] == msgDigest[ind:ind+4]:	#check if there is a running code in generated digest or no
			print("Key = " + ''.join(v))
			break
	else:
		print("[-] Solution not found")