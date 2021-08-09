def swapFunc(givenArray, len_array, j_value):
	i = 0
	newArr = givenArray
	while 1:
		res = len_array - j_value + 1
		if i >= res:
			break
		tmp = newArr[i]
		newArr[i] = givenArray[i + j_value - 1]
		newArr[i + j_value - 1] = tmp
		i  += j_value
	return newArr

def sortArrayWithOption(arr, len_array, opt):
	if opt == -1:
		for i in range(len_array - 1, 0, -1):
			arr = swapFunc(arr, len_array, i)
	elif opt == 1:
		j = 1
		while 1:
			if len_array <= j:
				break
			arr = swapFunc(arr, len_array, j)
			j+=1

def decodeFlag(arr):
	key = []
	i_value = []
	for i in range(180154381, 0xdeadbeef, 2075469):
		i_value.append(i)
	i_value = i_value[::-1]

	for i in i_value:
		keyStr = hex(i)[2:]
		len_keyStr = len(keyStr)
		completedKeyStr = '0'*(8 - len_keyStr) + keyStr
		key = list(bytearray.fromhex(completedKeyStr))
		for j in range(0, 30):
			arr[j] ^= key[j&3]
	return arr

def main():
	given = '7A 2E 6E 68 1D 65 16 7C 6D 43 6F 36 32 62 12 16 43 34 40 3E 58 01 58 3F 62 3F 53 30 6E 17'
	given = bytearray.fromhex(given)
	given = list(given)

	sortArrayWithOption(given, 30, -1)
	flag = decodeFlag(given)
	for i in flag:
		print(chr(i), end ='')
	print()

main()