from struct import unpack

def calc(i, rsi, rdx):
	v4 = rsi
	v5 = i % rdx
	v6 = 1
	while ( v4 ):
		if ( v4 & 1 ):
			v6 = v5 * v6 % rdx
		v5 = v5 * v5 % rdx
		v4 >>= 1
	return v6

def getList(byteArray, size):
	arr = []
	for i in range(0, len(byteArray), size):
		if size == 8:
			arr.append(unpack('<LL', byteArray[i:i+size])[0])
		elif size == 4:
			arr.append(unpack('<I', byteArray[i:i+size])[0])
	return arr

table0 	= bytearray()
table0 += bytearray.fromhex('08 20 00 00 00 00 00 00  28 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('28 20 00 00 00 00 00 00  08 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('40 20 00 00 00 00 00 00  62 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('08 20 00 00 00 00 00 00  40 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('40 20 00 00 00 00 00 00  62 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('28 20 00 00 00 00 00 00  40 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('62 20 00 00 00 00 00 00  28 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('62 20 00 00 00 00 00 00  40 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('62 20 00 00 00 00 00 00  08 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('40 20 00 00 00 00 00 00  40 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('40 20 00 00 00 00 00 00  08 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('40 20 00 00 00 00 00 00  08 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('62 20 00 00 00 00 00 00  62 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('28 20 00 00 00 00 00 00  08 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('28 20 00 00 00 00 00 00  62 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('40 20 00 00 00 00 00 00  62 20 00 00 00 00 00 00')
table0 += bytearray.fromhex('62 20 00 00 00 00 00 00 ')

args0 	= bytearray()
args0  += bytearray.fromhex('EB 7D 8A 4B 3D 00 00 00  8B 00 00 00 E6 01 00 00')
args0  += bytearray.fromhex('1E 00 00 00 6E 00 00 00  77 4D 04 72 77 00 00 00')
args0  += bytearray.fromhex('91 C3 00 00 43 01 00 00  11 03 00 00 13 00 00 00')
args0  += bytearray.fromhex('AA 62 27 76 0D 00 00 00  10 11 00 00 06 00 00 00')
args0  += bytearray.fromhex('AC AD 00 00 C3 00 00 00  71 03 00 00 17 00 00 00')
args0  += bytearray.fromhex('CD 00 00 00 E3 01 00 00  08 58 03 00 14 01 00 00')
args0  += bytearray.fromhex('78 00 00 00 13 00 00 00  14 00 00 00 E8 01 00 00')
args0  += bytearray.fromhex('22 02 00 00 16 00 00 00  00 1D 00 00 00 01 00 00')
args0  += bytearray.fromhex('34 00 00 00 12 00 00 00  D7 0C E2 45 67 01 00 00')
args0  += bytearray.fromhex('18 4E 03 00 2C 01 00 00  00 00 00 00 E6 01 00 00')
args0  += bytearray.fromhex('FD 0E 01 00 91 01 00 00  51 5E 43 79 BE 00 00 00')
args0  += bytearray.fromhex('27 2B 01 00 89 00 00 00  D1 33 33 33 05 00 00 00')
args0  += bytearray.fromhex('20 00 00 00 0C 00 00 00  1E 03 00 00 06 00 00 00')
args0  += bytearray.fromhex('2D 00 00 00 DB 01 00 00  A5 80 84 1F 8E 01 00 00')
args0  += bytearray.fromhex('48 01 00 00 DA 01 00 00  85 00 00 00 07 00 00 00')
args0  += bytearray.fromhex('DB 6F 03 00 05 01 00 00  B0 00 00 00 1B 00 00 00')
args0  += bytearray.fromhex('0D 00 00 00 0C 00 00 00')



def func_2008_mul(arg1, arg2):
	return (arg1*arg2)

def func_2028_add(arg1, arg2):
	return arg1 + arg2

def func_2062_sub(arg1, arg2):
	return arg1 - arg2

def func_2040_div(arg1, arg2):
	return arg1// arg2

if __name__ == '__main__':
	args_0 = getList(args0, 4)
	table_0= getList(table0,8)
	print(args_0)
	print(table_0)

	diffFuncs = []
	#get the number of different functions
	for i in table_0:
		if i not in diffFuncs:
			diffFuncs.append(i)
	print(len(diffFuncs))
	for i in diffFuncs:
		print(hex(i))


	#get target array
	target = []
	for i in range(0, len(table_0)):
		tmp1 = calc(i, 0x35, 0x383)
		tmp2 = calc(tmp1, 0x43, 0x383)
		target.append(tmp2)


	#get right order of args0 array
	order = []
	for i in range(0, 33):
		tmp_order = []
		for k in range(0, len(args_0), 2):
			arg1 = args_0[k]
			arg2 = args_0[k+1]

			#nếu như cặp tham số nào tính toán ra giống với target tại vị trí i thì thêm vào order
			#nếu như một giá trị target mà có nhiều tham số tính toán ra giống, thì cx thêm vào
			#sau đó, dùng số lượng mỗi loại hàm có trong table_0, mà loại trừ bớt đi
			res = func_2008_mul(arg1, arg2)&0xffff
			if res == target[i]:
				tmp_order.append(k//2)
			res = func_2028_add(arg1, arg2)&0xffff			#chỉ lấy 2 byte vì để ý thấy hàm calc thực ra làm hàm powmod
															#vì vậy nên giá trị trong target sẽ đều < 0x383( giá trị mod)
			if res == target[i]:
				tmp_order.append(k//2)
			res = func_2040_div(arg1, arg2)&0xffff
			if res == target[i]:
				tmp_order.append(k//2)
			res = func_2062_sub(arg1, arg2)&0xffff
			if res == target[i]:
				tmp_order.append(k//2)

		order.append(tmp_order)
	print("\n\t\t---------order:---------\t\t\n",order)

	#các vị trí đã được xác định và các vị trí chưa đưuọc xác định
	check = [0 for i in range(33)]
	for i in order:
		if(len(i) == 1):
			check[i[0]] = 1
	print("\t\t---------Các vị trí chưa được xác định:---------\t\t")
	for ind, val in enumerate(check):
		if val ==0:
			print(ind, end = ' ')
	print()
	#OUTPUT - order:
	#[[1, 2, 10, 13, 15, 19, 19, 26, 28], [32, 32], [29], [17], [3], [31], [30], [24], [12], [23], [11], [26], [9], [16], [18], [7], [2, 29], [5], [14], [27], [0], [13], [25], [6], [8], [1], [10], [28], [20], [15], [21], [4], [22]]

	order[1] 	= [32]	#vì cùng một tham số args[32] với 2 phép toán khác nhau cho ra cùng target[1]
	order[16] 	= [2]	#[2, 29], nhưng args[29] đã xác định tại vị trí khác nên ở đây dành cho 2
	order[0] 	= [19]	#ở vị trí 0, nhiều tham số cho ra cùng target[0], nhưng chỉ có args[19] là chưa có vị trí, nên dễ dàng suy ra điều này

	rightOrder = [i[0] for i in order]
	print("\t\t---------Order chinh xac được xác định:---------\t\t")
	print(rightOrder)
	table1  = bytearray() 
	table1 += bytearray.fromhex('40 20 00 00 00 00 00 00  40 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('40 20 00 00 00 00 00 00  28 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('62 20 00 00 00 00 00 00  62 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('40 20 00 00 00 00 00 00  28 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('40 20 00 00 00 00 00 00  40 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('40 20 00 00 00 00 00 00  40 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('62 20 00 00 00 00 00 00  40 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('62 20 00 00 00 00 00 00  28 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('62 20 00 00 00 00 00 00  28 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('40 20 00 00 00 00 00 00  28 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('62 20 00 00 00 00 00 00  40 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('28 20 00 00 00 00 00 00  40 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('28 20 00 00 00 00 00 00  40 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('40 20 00 00 00 00 00 00  28 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('28 20 00 00 00 00 00 00  28 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('28 20 00 00 00 00 00 00  62 20 00 00 00 00 00 00')
	table1 += bytearray.fromhex('28 20 00 00 00 00 00 00')

	args1 	= bytearray()
	args1  += bytearray.fromhex('30 03 00 00 10 00 00 00  71 57 00 00 97 01 00 00')
	args1  += bytearray.fromhex('28 71 00 00 1C 01 00 00  24 00 00 00 22 00 00 00')
	args1  += bytearray.fromhex('D7 00 00 00 A1 00 00 00  A4 01 00 00 71 01 00 00')
	args1  += bytearray.fromhex('BC 07 00 00 14 00 00 00  0B 00 00 00 27 00 00 00')
	args1  += bytearray.fromhex('AC 4E 00 00 7C 01 00 00  CC 33 00 00 04 01 00 00')
	args1  += bytearray.fromhex('8D 68 00 00 09 01 00 00  DA 35 00 00 71 00 00 00')
	args1  += bytearray.fromhex('0E 02 00 00 94 01 00 00  E0 38 00 00 04 01 00 00')
	args1  += bytearray.fromhex('5E 00 00 00 2C 00 00 00  1B 00 00 00 17 00 00 00')
	args1  += bytearray.fromhex('23 01 00 00 EB 00 00 00  51 00 00 00 03 00 00 00')
	args1  += bytearray.fromhex('47 37 00 00 0B 01 00 00  44 00 00 00 05 00 00 00')
	args1  += bytearray.fromhex('9E 01 00 00 3C 01 00 00  0B 4F 00 00 63 01 00 00')
	args1  += bytearray.fromhex('0D 00 00 00 70 00 00 00  A4 58 00 00 BA 00 00 00')
	args1  += bytearray.fromhex('41 00 00 00 39 00 00 00  E2 04 00 00 19 00 00 00')
	args1  += bytearray.fromhex('B4 4B 00 00 CC 00 00 00  06 00 00 00 32 00 00 00')
	args1  += bytearray.fromhex('23 00 00 00 11 00 00 00  23 00 00 00 20 00 00 00')
	args1  += bytearray.fromhex('58 00 00 00 22 00 00 00  6D 02 00 00 F2 01 00 00')
	args1  += bytearray.fromhex('0F 00 00 00 3B 00 00 00')

	table_1 = getList(table1, 8)
	args_1	= getList(args1, 4)

	rightTable1 = [0 for i in range(33)]
	rightArgs1 	= [0 for i in range(33*2)] 
	#sắp xếp lại vị trí của table1 và args1 cho chính xác
	for i in range(0, 33):
		rightTable1[i] 		= table_1[rightOrder[i]]
		rightArgs1[2*i]	 	= args_1[2*rightOrder[i]]
		rightArgs1[2*i + 1] = args_1[2*rightOrder[i] + 1]

	#decode flag
	flag = ''
	for i in range(0, len(rightTable1)):
		arg1 = rightArgs1[i*2]
		arg2 = rightArgs1[i*2 + 1]
		if rightTable1[i] == 0x2028:
			flag += chr(func_2028_add(arg1, arg2)&0xff)
		elif rightTable1[i] == 0x2062:
			flag += chr(func_2062_sub(arg1, arg2)&0xff)
		elif rightTable1[i] == 0x2008:
			flag += chr(func_2008_mul(arg1, arg2)&0xff)
		elif rightTable1[i] == 0x2040:
			flag += chr(func_2040_div(arg1, arg2)&0xff)
		else:
			print('Error')
			print(hex(rightTable1[i]))

	print(flag)
