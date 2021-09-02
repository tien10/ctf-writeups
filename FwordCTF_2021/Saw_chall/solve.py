
def getFlag(function):
	global flag
	lines = function
	flagInd = 0
	#get flagIndex in flag 								ex: mov     cx, [edi+16Bh]
	getIndLine = lines[0]
	if '[edi]' in getIndLine:
		flagInd = 0
	else:
		flagIndComp = getIndLine.split(',')[1]
		flagIndComp = flagIndComp.replace('h', '')
		flagIndComp = flagIndComp.replace('[edi+', '')
		flagIndComp = flagIndComp.replace(']', '')
		flagInd = int(flagIndComp, 16)

	#get bitIndex 										ex: shr     cx, 0
	checkBitLine = lines[1]
	checkBitComp = checkBitLine.split(',')[1]
	bitInd = int(checkBitComp)

	#get bit 											cmp     cx, 1
	bitLine = lines[3]
	bit = int(bitLine.split(',')[1])

	flag[flagInd][7 - bitInd] = bit
	return



flag = [[0 for i in range(0, 8)] for i in range(0, 400)] 
functions = []
def getConstraints():
	global functions

	f = open('checkFlagFunc.asm', 'r')
	lines = f.read()
	lines = lines.split('\n')
	length = len(lines)
	func = []

	for line in lines:
		if 'mov     eax, 1' in line or  'mov     esp, ebp' in line or 'pop     ebp' in line or 'retn' in line:
			break
		if 'mov     cx,' in line:
			func.append(line)
		if 'shr     cx,' in line:
			func.append(line)
		if 'and     cx,' in line:
			func.append(line)
		if 'cmp     cx,' in line:
			func.append(line)
		if 'jnz' in line:
			functions.append(func)
			func = []
	return

if __name__ == '__main__':
	getConstraints()
	for func in functions:
		getFlag(func)

	flagStr = ''
	for charArr in flag:
		s = ''.join(str(i) for i in charArr)
		flagStr += chr(int(s, 2))
	print(flagStr)
	return 

