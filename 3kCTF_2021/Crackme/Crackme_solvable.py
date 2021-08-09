Sample = [['xor', 'add'], ['not', 'xor', 'add'], ['assign_reg', 'xor', 'and', 'shl', 'assign_reg', 'add', 'add', 'and', 'or', 'add', 'assign_reg', 'assign_reg'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['assign_reg', 'xor', 'not', 'add', 'add']]

allFunction = [['xor', 'add'], ['not', 'xor', 'add'], ['assign_reg', 'xor', 'and', 'shl', 'assign_reg', 'add', 'add', 'and', 'or', 'add', 'assign_reg', 'assign_reg'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['assign_reg', 'xor', 'not', 'add', 'add'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['xor', 'add'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['xor', 'add'], ['not', 'xor', 'add'], ['not', 'xor', 'add'], ['assign_reg', 'xor', 'and', 'shl', 'assign_reg', 'add', 'add', 'and', 'or', 'add', 'assign_reg', 'assign_reg'], ['not', 'xor', 'add'], ['xor', 'add'], ['not', 'xor', 'add'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['xor', 'add'], ['assign_reg', 'xor', 'and', 'shl', 'assign_reg', 'add', 'add', 'and', 'or', 'add', 'assign_reg', 'assign_reg'], ['xor', 'add'], ['not', 'xor', 'add'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['assign_reg', 'xor', 'and', 'shl', 'assign_reg', 'add', 'add', 'and', 'or', 'add', 'assign_reg', 'assign_reg'], ['not', 'xor', 'add'], ['assign_reg', 'xor', 'and', 'shl', 'assign_reg', 'add', 'add', 'and', 'or', 'add', 'assign_reg', 'assign_reg'], ['not', 'xor', 'add'], ['xor', 'add'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['assign_reg', 'xor', 'and', 'shl', 'assign_reg', 'add', 'add', 'and', 'or', 'add', 'assign_reg', 'assign_reg'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['not', 'xor', 'add'], ['not', 'xor', 'add'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['not', 'xor', 'add'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['assign_reg', 'xor', 'and', 'shl', 'assign_reg', 'add', 'add', 'and', 'or', 'add', 'assign_reg', 'assign_reg'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['not', 'xor', 'add'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['assign_reg', 'xor', 'and', 'shl', 'assign_reg', 'add', 'add', 'and', 'or', 'add', 'assign_reg', 'assign_reg'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['not', 'xor', 'add'], ['assign_reg', 'xor', 'and', 'mul', 'add', 'add'], ['not', 'xor', 'add']]

imm = [186, 145, 139, 154, 141, 223, 139, 151, 154, 223, 153, 147, 158, 152, 197, 223, 99, 139, 138, 16, 133, 138, 1, 142, 116, 139, 204, 148, 95, 146, 203, 237, 176, 151, 105, 145, 155, 95, 80, 64, 114, 207, 140, 27, 128, 156, 60, 80, 150, 111, 146, 64, 97, 151, 140, 160, 141, 144, 145, 64, 97, 206, 207, 207, 144, 64, 161, 135, 188, 130, 71, 111, 111, 100, 32, 74, 111, 98, 10, 84, 114, 121, 32, 97, 103, 97, 105, 110, 10]

params = [[16], [17], [18, 19, 1], [20, 2], [21, 2], [22], [23, 2], [24], [25, 2], [26, 2], [27, 2], [28], [29], [30], [31, 32, 1], [33], [34], [35], [36, 2], [37], [38, 39, 1], [40], [41], [42, 2], [43, 44, 1], [45], [46, 47, 1], [48], [49], [50, 2], [51, 52, 1], [53, 2], [54], [55], [56, 2], [57], [58, 2], [59, 60, 1], [61, 2], [62], [63, 2], [64, 65, 1], [66, 2], [67], [68, 2], [69]]
def solveFuncSample1(imm):		#['xor', 'add'] - Sample[0]
	return chr(imm)
def solveFuncSample2(imm):		#['not', 'xor', 'add'] - Sample[1]
	return chr((0xffffffff + 1 + ~imm)&0xff)
	
#['assign_reg', 'xor', 'and', 'shl', 'assign_reg', 'add', 'add', 'and', 'or', 'add', 'assign_reg', 'assign_reg'] - Sample[2]
def solveFuncSample3(imm1, imm2, shift):
	#print("imm1", imm1)
	#print("imm2", imm2)
	#print("shift", shift)

	for x in range(33, 126):
		char = x
		tmp1 = x 					#stack[1] = stack[0]
		
		x ^= imm1					#stack[0] ^= imm1
		#print("s[0] sau xor: ", hex(x))
		tmp1 = tmp1 & imm1
		#print("s[1] sau and: ", hex(tmp1))
		
		tmp1 = (tmp1 << shift)&0xff
		#print(hex(tmp1 ))
		tmp2 = tmp1
		tmp1 = (tmp1 + x) &0xff
		#print('tmp1 sau add: ', hex(tmp1 ))

		tmp2 = (tmp2 + x) &0xff
		#print('tmp2 sau add: ', hex(tmp2))
		
		tmp1 &= imm2
		tmp1 |= imm2
		tmp1 = (tmp1 +tmp2)&0xff
		if tmp1 == 0:
			#print(chr(x))
			return chr(char)


#['assign_reg', 'xor', 'and', 'mul', 'add', 'add'] - Sample[3]
def solveFuncSample4(imm, mul):
	for x in range(33, 126):
		if ((x^imm) + ((x&imm) * mul))&0xff == 0:
			return chr(x)

#['assign_reg', 'xor', 'not', 'add', 'add'] - Sample[4]
def solveFuncSample5(imm):
	res = []
	for i in range(33, 126):
		tmp = ((~(i ^1)&0xff) + i) & 0xff
		if tmp == 0:
			res.append(chr(i))
	return res


if __name__ == '__main__':
	flag = ''
	for i in Sample:
		print(i)
	for i in range(0, len(allFunction)):


		if allFunction[i] == Sample[0]:
			char = solveFuncSample1(imm[params[i][0]])
			flag += char
			print("i: ", char)

		elif allFunction[i] == Sample[1]:
			char = solveFuncSample2(imm[params[i][0]])
			flag += char
			print("i: ", char)

		elif allFunction[i] == Sample[2]:
			char = solveFuncSample3(imm[params[i][0]], imm[params[i][1]], params[i][2])
			flag += char
			print("i: ", char)

		elif allFunction[i] == Sample[3]:
			char = solveFuncSample4(imm[params[i][0]], params[i][1])
			flag += char
			print("i: ", char)

		elif allFunction[i] == Sample[4]:
			char = []
			char = solveFuncSample5(imm[params[i][0]])
			flag += "*"
			print("i: ", char)

	print(flag)

