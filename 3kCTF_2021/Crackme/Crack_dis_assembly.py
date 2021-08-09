if __name__ == '__main__':
	imm = [186, 145, 139, 154, 141, 223, 139, 151, 154, 223, 153, 147, 158, 152, 197, 223, 99, 139, 138, 16, 133, 138, 1, 142, 116, 139, 204, 148, 95, 146, 203, 237, 176, 151, 105, 145, 155, 95, 80, 64, 114, 207, 140, 27, 128, 156, 60, 80, 150, 111, 146, 64, 97, 151, 140, 160, 141, 144, 145, 64, 97, 206, 207, 207, 144, 64, 161, 135, 188, 130, 71, 111, 111, 100, 32, 74, 111, 98, 10, 84, 114, 121, 32, 97, 103, 97, 105, 110, 10]


	bytecode = [6, 0, 0, 6, 1, 1, 6, 2, 2, 6, 3, 3, 3, 0, 0, 3, 1, 0, 3, 2, 0, 3, 3, 0, 8, 0, 0, 5, 0, 1, 8, 0, 0, 5, 0, 2, 8, 0, 0, 5, 0, 3, 8, 0, 0, 6, 0, 4, 6, 1, 5, 6, 2, 6, 6, 3, 7, 3, 0, 0, 3, 1, 0, 3, 2, 0, 3, 3, 0, 8, 0, 0, 5, 0, 1, 8, 0, 0, 5, 0, 2, 8, 0, 0, 5, 0, 3, 8, 0, 0, 6, 0, 8, 6, 1, 9, 6, 2, 10, 6, 3, 11, 3, 0, 0, 3, 1, 0, 3, 2, 0, 3, 3, 0, 8, 0, 0, 5, 0, 1, 8, 0, 0, 5, 0, 2, 8, 0, 0, 5, 0, 3, 8, 0, 0, 6, 0, 12, 6, 1, 13, 6, 2, 14, 6, 3, 15, 3, 0, 0, 3, 1, 0, 3, 2, 0, 3, 3, 0, 8, 0, 0, 5, 0, 1, 8, 0, 0, 5, 0, 2, 8, 0, 0, 5, 0, 3, 8, 0, 0, 6, 3, 0, 4, 3, 0, 10, 0, 0, 4, 0, 16, 14, 3, 0, 10, 0, 0, 3, 0, 0, 4, 0, 17, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 0, 18, 12, 1, 18, 11, 1, 1, 5, 2, 1, 14, 1, 0, 14, 2, 0, 12, 1, 19, 13, 2, 19, 14, 1, 2, 5, 0, 1, 5, 3, 1, 10, 0, 0, 5, 1, 0, 4, 1, 20, 12, 0, 20, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 1, 21, 12, 0, 21, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 0, 22, 3, 0, 0, 14, 0, 1, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 1, 23, 12, 0, 23, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 4, 0, 24, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 1, 25, 12, 0, 25, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 1, 26, 12, 0, 26, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 1, 27, 12, 0, 27, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 4, 0, 28, 14, 3, 0, 10, 0, 0, 3, 0, 0, 4, 0, 29, 14, 3, 0, 10, 0, 0, 3, 0, 0, 4, 0, 30, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 0, 31, 12, 1, 31, 11, 1, 1, 5, 2, 1, 14, 1, 0, 14, 2, 0, 12, 1, 32, 13, 2, 32, 14, 1, 2, 5, 0, 1, 5, 3, 1, 10, 0, 0, 3, 0, 0, 4, 0, 33, 14, 3, 0, 10, 0, 0, 4, 0, 34, 14, 3, 0, 10, 0, 0, 3, 0, 0, 4, 0, 35, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 1, 36, 12, 0, 36, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 4, 0, 37, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 0, 38, 12, 1, 38, 11, 1, 1, 5, 2, 1, 14, 1, 0, 14, 2, 0, 12, 1, 39, 13, 2, 39, 14, 1, 2, 5, 0, 1, 5, 3, 1, 10, 0, 0, 4, 0, 40, 14, 3, 0, 10, 0, 0, 3, 0, 0, 4, 0, 41, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 1, 42, 12, 0, 42, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 0, 43, 12, 1, 43, 11, 1, 1, 5, 2, 1, 14, 1, 0, 14, 2, 0, 12, 1, 44, 13, 2, 44, 14, 1, 2, 5, 0, 1, 5, 3, 1, 10, 0, 0, 3, 0, 0, 4, 0, 45, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 0, 46, 12, 1, 46, 11, 1, 1, 5, 2, 1, 14, 1, 0, 14, 2, 0, 12, 1, 47, 13, 2, 47, 14, 1, 2, 5, 0, 1, 5, 3, 1, 10, 0, 0, 3, 0, 0, 4, 0, 48, 14, 3, 0, 10, 0, 0, 4, 0, 49, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 1, 50, 12, 0, 50, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 0, 51, 12, 1, 51, 11, 1, 1, 5, 2, 1, 14, 1, 0, 14, 2, 0, 12, 1, 52, 13, 2, 52, 14, 1, 2, 5, 0, 1, 5, 3, 1, 10, 0, 0, 5, 1, 0, 4, 1, 53, 12, 0, 53, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 3, 0, 0, 4, 0, 54, 14, 3, 0, 10, 0, 0, 3, 0, 0, 4, 0, 55, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 1, 56, 12, 0, 56, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 3, 0, 0, 4, 0, 57, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 1, 58, 12, 0, 58, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 0, 59, 12, 1, 59, 11, 1, 1, 5, 2, 1, 14, 1, 0, 14, 2, 0, 12, 1, 60, 13, 2, 60, 14, 1, 2, 5, 0, 1, 5, 3, 1, 10, 0, 0, 5, 1, 0, 4, 1, 61, 12, 0, 61, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 3, 0, 0, 4, 0, 62, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 1, 63, 12, 0, 63, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 0, 64, 12, 1, 64, 11, 1, 1, 5, 2, 1, 14, 1, 0, 14, 2, 0, 12, 1, 65, 13, 2, 65, 14, 1, 2, 5, 0, 1, 5, 3, 1, 10, 0, 0, 5, 1, 0, 4, 1, 66, 12, 0, 66, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 3, 0, 0, 4, 0, 67, 14, 3, 0, 10, 0, 0, 5, 1, 0, 4, 1, 68, 12, 0, 68, 1, 0, 2, 14, 0, 1, 14, 3, 0, 10, 0, 0, 3, 0, 0, 4, 0, 69, 14, 3, 0, 5, 0, 3, 7, 66, 0, 6, 0, 70, 8, 0, 0, 6, 0, 71, 8, 0, 0, 6, 0, 72, 8, 0, 0, 6, 0, 73, 8, 0, 0, 6, 0, 74, 8, 0, 0, 6, 0, 75, 8, 0, 0, 6, 0, 76, 8, 0, 0, 6, 0, 77, 8, 0, 0, 6, 0, 78, 8, 0, 0, 6, 0, 0, 4, 0, 0, 9, 0, 0, 6, 0, 79, 8, 0, 0, 6, 0, 80, 8, 0, 0, 6, 0, 81, 8, 0, 0, 6, 0, 82, 8, 0, 0, 6, 0, 83, 8, 0, 0, 6, 0, 84, 8, 0, 0, 6, 0, 85, 8, 0, 0, 6, 0, 86, 8, 0, 0, 6, 0, 87, 8, 0, 0, 6, 0, 88, 8, 0, 0, 6, 0, 0, 9, 0, 0]



	#opcode: instruction
	instruction = {	1:'mul',		\
					2:'sub',		\
					3:'not', 		\
					4:'xor',		\
					5:'assign_reg',	\
					6:'assign_imm',	\
					7:'if',			\
					8:'putc',		\
					9:'exit',		\
					10:'getc',		\
					11:'shl',		\
					12:'and',		\
					13:'or',		\
					14:'add'}
	ins_gr1 = [3, 8, 7, 9, 10]
	ins_gr2 = [1, 2, 11]
	ins_gr3 = [5, 14]
	ins_gr4 = [4, 6, 12, 13]
	#có 4 nhóm câu lệnh: 
	#reg: 			not, putc, getc, exit, if
	#reg - arg2: 	mul, sub, shl
	#reg - reg:		assign_reg, add	
	#reg - imm:		xor, assign_imm, and, or
	params = []
	insOfSomeFunc = []
	pc = 0
	while pc < len(bytecode):
		opcode = bytecode[pc]

		if opcode <= 0 and opcode >= 15:
			print('[+] Illegal Instruciton')
			break
		else:
			disass = "%04x: %s" %(pc, instruction[opcode])
			opr1 = bytecode[pc + 1]
			opr2 = bytecode[pc + 2]
			if opcode in ins_gr1:	#reg:
				if opcode == 10:
					print('\n\n\t\t-----------GETC-----------\t\t')

					tmp = pc + 3
					sample = []
					#lệnh tại pc = 0x43b vai trò như là get kết thúc
					while tmp < len(bytecode) and bytecode[tmp] != 10 and tmp != 0x043b:
						sample.append(instruction[bytecode[tmp]])
						tmp += 3
					
					insOfSomeFunc.append(sample)
					if len(sample) == 2:		#[xor', 'add']
						param = []
						param.append(bytecode[pc + 3 + 2])			#imm
						params.append(param)
					elif len(sample) == 3:		#['not', 'xor', 'add']
						param = []
						param.append(bytecode[pc + 3+ 3 + 2])			#imm
						params.append(param)
					#['assign_reg', 'xor', 'and', 'shl', 'assign_reg', 'add', 'add', 'and', 'or', 'add', 'assign_reg', 'assign_reg']
					elif len(sample) == 12:
						param = []
						param.append(bytecode[pc + 3*2 + 2])			#imm1
						param.append(bytecode[pc + 3*8 + 2])			#imm2
						param.append(bytecode[pc + 3*4 + 2])			#shift
						params.append(param)
					#['assign_reg', 'xor', 'and', 'mul', 'add', 'add'] - Sample[3]
					elif len(sample) == 6:
						param = []
						param.append(bytecode[pc + 3*2 + 2])			#imm
						param.append(bytecode[pc + 3*4 + 2])			#mul
						params.append(param)
					#['assign_reg', 'xor', 'not', 'add', 'add'] - Sample[4]
					elif len(sample) == 5:
						param = []
						param.append(bytecode[pc + 3*2 + 2])			#imm
						params.append(param)



				elif opcode == 3:
					disass = "%s( %s)" %(disass, "reg[" + str(opr1)+"]")
				elif opcode == 7:		#if reg[0] == 0? pc += 3:pc += opr1
					print('\n\n\t\t-----------BRANCH?-----------\t\t')
					disass = "%s (reg[0] == 0)?PC = %04x:PC = %04x" %(disass, pc + 3, pc + opr1)
				else:
					disass = "%s(reg[0])" %(disass)

				print(disass)
				if opcode == 9:
						print('\n\t\t+++++++++++++END+++++++++++++\t\t\n')
			elif opcode in ins_gr2:	#reg - arg2:
				disass = "%s( %s, %d)" %(disass, "reg["+str(opr1)+"]", opr2)
				print(disass)

			elif opcode in ins_gr3:	#reg - reg:
				disass = "%s( %s, %s)" %(disass, "reg["+str(opr1)+"]", "reg["+str(opr2)+"]")
				print(disass)

			elif opcode in ins_gr4:	#reg - imm
				
				immediate = imm[opr2]
				if pc > 0x043e:
					if bytecode[pc + 3] == 4 or bytecode[pc + 3] == 9:	#xor
						disass = "%s( %s, %x)" %(disass, "reg["+str(opr1)+"]", immediate)
					else:
						disass = "%s( %s, %s)" %(disass, "reg["+str(opr1)+"]", chr(immediate))

				else:
					disass = "%s( %s, %d)" %(disass, "reg["+str(opr1)+"]", immediate)
				
				print(disass)

			pc += 3

	
	print(insOfSomeFunc)
	print(params)
