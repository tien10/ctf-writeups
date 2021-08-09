def getOriginalWord(not_flag, word, option):
	ind = 0
	for i in range(0, len(not_flag), 2):
		tmp = (not_flag[i + 1]<<8)&0xffff | not_flag[i]
		if tmp == word:
			ind = i
			break
	ind //= 2
	if option == 0xdead:
		return ind^0xbeef
	elif option == 0x1337:
		return ind^0xcafe

def recover(not_flag, arr, option):
	arrRet = [0 for i in range(40)]
	if option == 0x1337:
		for i in range(0, 40):

			tmp = arr[i] ^ 0x00001337
			lowWord = tmp&0xffff
			originalLowWord = getOriginalWord(not_flag, lowWord, option)
			highWord = (tmp>>16)&0xffff
			originalHighWord = getOriginalWord(not_flag, highWord, option)
			ele = (originalHighWord <<16)&0xffffffff | originalLowWord
			arrRet[i] = ele
	elif option == 0xdead:	
		for i in range(0, 40):

			tmp = arr[i] ^ 0x0000dead
			lowWord = tmp&0xffff
			originalLowWord = getOriginalWord(not_flag, lowWord, option)
			highWord = (tmp>>16)&0xffff
			originalHighWord = getOriginalWord(not_flag, highWord, option)
			ele = (originalHighWord <<16)&0xffffffff | originalLowWord
			arrRet[i] = ele
	return arrRet
def main():

	#	mảng các giá trị trong file encrypted_flag
	encrypted_flag = [1409347954, 2493272421, 3334227463, 3324106303, 3255568752, 4071879996, 2864408569, 4262361787, 1793355349, 3709938981, 4217904331, 787675392, 1977348036, 2766383325, 1013634282, 799627545, 1315797828, 3060509938, 2696392867, 3998743937, 1160383396, 2690484265, 93394560, 70905806, 1966369891, 3806909452, 2186616503, 23032049, 862307667, 1300821489, 514177195, 4204897454, 2438363542, 332962096, 1796578433, 897030716, 1569026986, 123275500, 193997444, 352442528]
	not_flag = open('not_flag', 'rb')
	byteArrOf_not_flag = not_flag.read()
	
	#compose2
	recoverArr1 = recover(byteArrOf_not_flag, encrypted_flag, 0xdead)
	recoverArr2 = recover(byteArrOf_not_flag, recoverArr1, 0x1337)

	#compose1
	recoverArr3 = recover(byteArrOf_not_flag, recoverArr2, 0x1337)
	recoverArr4 = recover(byteArrOf_not_flag, recoverArr3, 0xdead)
	for i in range(40):
		print(chr(recoverArr4[i]&0xff), end = '')
main()