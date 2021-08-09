from pwn import *
import re

def foo(a1, a2, missed_ind):
	'''
	miss: 1, 2, 3
	return a1 ^ (a2 + 1) ^ 0x539u;
	'''
	if missed_ind == 1:
		return a2^(a1 + 1)^0x539
	if missed_ind == 2:
		return (a2 ^ a1 ^ 0x539) - 1
	if missed_ind == 3:
		return a1 ^ (a2 + 1) ^ 0x539

def bar(a1, a2, a3, missed_ind):
	'''
	miss: 1, 2, 3, 4
	return (unsigned int)(a1 + a2 * (a3 + 1))
	'''
	if missed_ind == 1:
		return a3 - a1*(a2+1)
	if missed_ind == 2:
		return (a3 - a1)//(a2 + 1)
	if missed_ind == 3:
		return (a3 - a1)//a2 - 1
	if missed_ind == 4:
		return (a1 + a2*(a3 + 1)) & 0xffffffff

def getMissedIndex(dataStr, aArr):
	res = 0
	quesMarkPos = dataStr.find('?')
	ind = []
	ind.append(quesMarkPos)
	for i in aArr:
		ind.append(dataStr.find(i))
	ind.sort()
	for j in range(len(ind)):
		if ind[j] == quesMarkPos:
			return j + 1

def main():
	BINFILE = "./infinity_gauntlet"
	HOST = "shell.actf.co"
	PORT = 21700
	p = remote(HOST, PORT)


	i_xor = [(17*i)&0xff for i in range(26)]
	#print(i_xor)
	data2Flag = [i for i in range(26)]
	roundth = 1
	check = 1
	position = [0 for i in range(26)]

	while check:
		roundNotice = p.recvuntil("==\n")
		data = p.recvline()	#nhận phép toán
		dataStr = data.decode()
		#lấy các giá trị là số nguyên trong phép toán
		aArr = re.findall(r'\d+', dataStr)
		
		#missed chính là dấu chấm ?
		missed_ind = getMissedIndex(dataStr, aArr)
		res = 0
		if len(aArr) == 2:
			res = foo(int(aArr[0]), int(aArr[1]), missed_ind)
		elif len(aArr) == 3:
			res = bar(int(aArr[0]), int(aArr[1]), int(aArr[2]), missed_ind)

		if roundth>=50:
			posInFlag = ((res>>8)& 0xff) - roundth
			#print(roundth, posInFlag)
			if posInFlag <len(position) and position[posInFlag] == 0:
				position[posInFlag] = 1
				value = res&0xff
				value ^= i_xor[posInFlag]
				data2Flag[posInFlag] = chr(value)

		p.sendline(str(res))
		roundth +=1
		if position == [1 for i in range(26)]:
			check = 0
	flag = ''.join(data2Flag)
	print(flag)
	return


main()