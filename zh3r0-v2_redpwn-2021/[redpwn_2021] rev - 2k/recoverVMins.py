offsets = [4294963552, 4294963639, 4294963656, 4294963665, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963693, 4294963836, 4294963860, 4294963713, 4294963740, 4294963767, 4294963801, 4294963885, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963916, 4294963952, 4294964008, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294964043, 4294963530, 4294964071, 4294964113, 4294964155, 4294964171, 4294964188, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294964204, 4294964228, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294963552, 4294964252, 4294964263, 4294964274, 4294963626]
insType = []
for i in range(0, len(offsets)):
	if i not in insType:
		insType.append(0x21d0 - (0x100000000 - offsets[i]))

op_ins = {	0x131a: 'check st[top - 1] == 0',													#*\
			0x1330: 'nop',	\
			0x137a: 'cnt -= st[top]',	\
			0x1387: 'st[top] = stop[top - 1]',	\
			0x1398: 'pop',	\
			0x13a1: 'st[top] == 0: open flag',	\
			0x13bd: 'add: st[top - 1]   += st[top]',	\
			0x13d1: 'div: st[top - 1] 	= st[top] / st[top - 1]',	\
			0x13ec: 'mod: st[top - 1] 	= st[top] '+ "%" + ' st[top - 1]',	\
			0x1407: 'complex: st[top - 1] = (st[top - 1] * st[top]) +' "%" + 'st[top + 1]',	\
			0x1429: 'st[top -1] = (st[top - 1] == st[top])?1:0',								#*\
			0x144c: 'sub: st[top - 1] 	= st[top] - st[top -1]',	\
			0x1464: 'mul: st[top - 1] 	= st[top] * st[top -1]',	\
			0x147d: 'st[top] = (st[top] < 0)?-1:1',												#*\
			0x149c: 'get char',	\
			0x14c0: 'printf char',	\
			0x14f8: 'push ',																	#push opcodes[r13]\
			0x151b: 'init rdx',	\
			0x1537: 'if st[top - 1] != 0: init rdx',											#*\
			0x1561: 'cmp st[top - 1], 0, js == true: init rdx',									#*\
			0x158b: 'st[top -1] > 0: init rdx',													#*\
			0x159b: 'st[top -1] < 0: init rdx',													#*\
			0x15ac: 'cmp st[top - 1], 0, jns == true: init rdx',								#*\
			0x15bc: 'store',	\
			0x15d4: 'load',	\
			0x15ec: 'cnt += 1',	\
			0x15f7: 'cnt -= 1',	\
			0x1602: 'cnt += st[top]'	\
		}
f = open('prog.bin', 'rb')
data = f.read()
data = bytearray(data)
opcodes = list(data)

rax = 0
rdx = 0
r13 = 0
disassStr = ''
cnt = 0 				#check len input
while rdx < 0x2fdb:
	rax = rdx
	r13 = rdx + 1

	ins = opcodes[rax]

	if ins > 83:
		rdx = r13
		nop_ins = "%04x: %s" %(rax, op_ins[0x1330])
		disassStr += nop_ins + '\n'
	else:
		tmp = 0x21d0 - (0x100000000 - offsets[ins])
		if tmp == 0x149c:
			cnt += 1
		disass = "%04x: %s" %(rax, op_ins[tmp])

		if tmp == 0x14f8:
			_disass = "%s%d" %(disass, opcodes[r13])
			disassStr += _disass+"\n"
			rdx += 3
		else:
			rdx = r13
			disassStr += disass + '\n'
		if tmp in [0x1537, 0x1561, 0x158b, 0x159b, 0x15ac] and rdx >0x230:
			disassStr += '\n\n\n'			#support you keep easily trace later function of disassembly code
print('Length of input( known getc() calling):', cnt)		#check length input
	
print(disassStr)