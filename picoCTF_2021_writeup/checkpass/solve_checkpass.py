from struct import unpack
from idc import GetManyBytes

def getTable():
	num = 1024
	size = 1
	address = 0x39560		#address of big Table T


	table = []
	for i in xrange(0, num, size):
		data= GetManyBytes(address + i, size)
		table.append(unpack('B', data)[0])

	return table

def getPermutation():
	num = 128
	size = 8
	address = 0x39970			#address of permutation array

	permutation = []
	for i in range(0, size*128, size):
		data = GetManyBytes(address + i, size)
		permutation.append(unpack('<Q', data)[0])
	return permutation

def recoverGeneratedArr_x(dstArr, x):
	x = x <<8
	recoverArr = [0]*32
	table = getTable()
	indexArr = getPermutation()
	stack = [0]*32
	for i in range(0, 32):
		tmp = stack[indexArr[x//8 + i]] = dstArr[i]
		for j in range(0, 256):
			if table[x+j] == tmp:
				recoverArr[indexArr[x//8 + i]] = j
				break
	return recoverArr

def main():
	target = [31, 43, 80, 70, 184, 34, 58, 203, 188, 122, 174, 203, 174, 32, 193,\
	72, 5, 123, 123, 58, 205, 184, 70, 158, 207, 230, 119, 158, 167, 1, 122, 123]
	
	
	generatedArr3 = target
	generatedArr2 = recoverGeneratedArr_x(generatedArr3, 3)
	generatedArr1 = recoverGeneratedArr_x(generatedArr2, 2)
	generatedArr0 = recoverGeneratedArr_x(generatedArr1, 1)
	userInput = recoverGeneratedArr_x(generatedArr0, 0)
	res = ''
	for i in userInput:
		res+=chr(i)
	print(res)

main()