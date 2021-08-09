arr = [0 for i in range(81)]
arr[4] = 1

def add(reg1, reg2, reg3):
	arr[reg1] = arr[reg2] + arr[reg3]
	return
def sub(reg1, reg2, reg3):
	arr[reg1] = arr[reg2] - arr[reg3]
	return
def mul(reg1, reg2, reg3):
	arr[reg1] = arr[reg2]*arr[reg3]
	return
def div(reg1, reg2, reg3):
	arr[reg1] = arr[reg2] // arr[reg3]
	return
def _read(reg1, reg2):
	arr[reg1] = arr[4 + arr[reg2]]
	return
def _write(reg1, reg2):
	arr[4 + arr[reg1]] = arr[reg2]
	return

def check(reg1):
	for i in range(4, 20):
		if arr[i + reg1] != ord(target[i - 4]):
			print('Undone')
			return
	print("Done")



target = '3p1cl337-k3yw0rd'
def debug():
	global DEBUG
	global REV

	print('arr[0] - tmp1:', arr[0])
	print('arr[1] - tmp2:', arr[1])
	print('arr[2] - tmp3:', arr[2])
	print('arr[3] - tmp4:', arr[3])
	if REV == 1:
		print('index:')
		print('\t'.join(str(i + 4) for i in range(0, 16)))
		print('res:')
		for i in range(4, 20):
			print(hex(arr[i])[2:], end = '\t')
		print()
		print('target:')
		for i in target:
			print(f"'{i}'{hex(ord(i))[2:]}", end ='\t')
		print()
	else:
		print('')
		for i in range(4, len(arr)):
			print(hex(arr[i])[2:], end = '  ')
		print()
	return

#------------------------------------------------------------------

import sys	
DEBUG 	= 0
REV 	= 0
def main():
	cnt = 0
	global DEBUG
	global REV
	print('1. For REV - Weird Interpreter')
	print('2. For PWN - Weird Interpreter')
					
	selection = input("Your option: ")
	if int(selection) == 1:
		REV = 1
	else:
		retAddr = input("Enter two LSB of return addr: ")
		arr[80] = int(retAddr, 16)

	print('1. Debugging and build instructions')
	print('2. Testing')
	selection1 = input("Your option: ")
	if int(selection1) == 1:
		DEBUG = 1
		print("\n\t\t---------------------DEBUG---------------------\t\t\n")
	else:
		if REV == 1:
			instructions = 'a144a114a<11m111m2<1s<21a004a100a201a302aA<2a6A0a461a961a:61a>61a;:3m761a770aC70m=;1s==2a8=0a583aB51a@B3a@@0a?@1s000c0'
			print("Your vm's instructions:", instructions)
		elif REV == 0:
			instructions = 'a144m111m111a004a000m000a004m101a204a344a334a223s212a334s113r31a004a000s220a332w13'
			print("Your vm's instructions:", instructions)
		ins_arry = []
		j = 0
		while j < len(instructions):
			if instructions[j] == 'a' or instructions[j] == 's' or instructions[j] == 'm' or instructions[j] == 'd':
				ins_arry.append(instructions[j:j+4])
				j += 4
			elif instructions[j] == 'r' or instructions[j] == 'w':
				ins_arry.append(instructions[j:j+3])
				j += 3
			elif instructions[j] == 'c':
				ins_arry.append(instructions[j:j+2])
				j += 2
			else:
				print("Error")
				return
	debug()

	#---------------------For TESTING
	

	while cnt <= 84:
		if DEBUG == 1:
			ins 	= input('input your instruction:')
		elif DEBUG == 0:
			if cnt >= len(ins_arry):
				return
			ins = ins_arry[cnt]

		#-----get opcode and register-------	
		opcode 	= ins[0]
		reg1  	= ord(ins[1]) - 48
		if len(ins) >= 3:
			reg2  	= ord(ins[2]) - 48
		if len(ins) >= 4:
			reg3  	= ord(ins[3]) - 48

		#-----vm activiy---------
		if opcode == 'a':
			add(reg1, reg2, reg3)
		if opcode == 's':
			sub(reg1, reg2, reg3)
		if opcode == 'm':
			mul(reg1, reg2, reg3)
		if opcode == 'd':
			div(reg1, reg2, reg3)
		if opcode == 'r':
			_read(reg1, reg2)
		if opcode == 'w':
			_write(reg1, reg2)
		if opcode == 'c':
			check(reg1)
			return

		debug()
		print()
		cnt +=1
		print('so luong opcode:', cnt)
		print("\t\t--------------------------------------------\t\t")


	return

if __name__ == '__main__':
	main()