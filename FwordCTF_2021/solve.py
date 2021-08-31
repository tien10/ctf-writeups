checkIndex = []			#index of junkcode which contains instruction setting r13 = 1
argArr = [] 			#Ex: mov     r11, 1A6232C39h, arg = 0x1A6232C39
target = []


def ror(num, rorNum):
	tmp = (num >> rorNum) & 0xffffffffffffffff | (num << (64 - rorNum)) & 0xffffffffffffffff
	return tmp


def getTarget():
	for i in range(0, len(argArr)):
		r11 = argArr[i] ^ 0x1337
		r11 = ror(r11, 0xd)
		if i in checkIndex:
			target.append(r11)
	return



def getArgArray():
	global checkIndex
	global argArr
	f = open('bytecode.asm', 'r')
	t = f.read()
	functions = t.split('; ---------------------------------------------------------------------------')

	for i in range(0, len(functions)):
	
		lines = functions[i].split('\n')
		for line in lines:
			if 'mov     r11,' in line:
				s = line
				comp = s.split(',')
				arg = int(comp[1].replace('h', ''), 16)
				argArr.append(arg)
			if 'mov     r13, 1' in line:
				checkIndex.append(i)

	return  


def bruteFlag():
	for i in range(0, len(target)):
		for ch in range(32, 126):
			tmp = ((ch + 1) << 10) ^ (ch + 1)
			value1 = (tmp >> 1) + tmp
			v10 = (((8 * value1) ^ value1) >> 5)
			v10 += ((8 * value1) ^ value1)
			v11 = (((16 * v10) ^ v10) >> 17) 
			v11 += ((16 * v10) ^ v10)
			v12 = (((v11 << 25) & 0xffffffff) ^ v11)
			valueCheck = v12 >> 6
			valueCheck = (valueCheck + v12) & 0xffffffff
			if valueCheck == target[i]:
				print(chr(ch),end = '')
	print()

if __name__ == '__main__':
	getArgArray()				#get arguments from disassembly code
	getTarget()					#pre-calculate all of values in r11 register

	bruteFlag()
#FWORDctf{W3_4t_th3_t0p_4g41n_n0w_wh4t?}