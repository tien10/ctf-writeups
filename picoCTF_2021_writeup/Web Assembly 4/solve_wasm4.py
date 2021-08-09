target = [24, 106, 124, 97, 17, 56, 105, 55, 70, 91, 35, 6, 102, 74, \
86, 58, 13, 28, 18, 47, 100, 100, 17, 86, 117, 15, 110, 27, 6, 56, \
7, 69, 16, 47, 111, 63, 19, 2, 43, 9, 94]
#target array after swap the target[i] and target[i + 1]
arr= [106, 24, 97, 124, 56, 17, 55, 105, 91, 70, 6, 35, 74, 102, 58, \
86, 28, 13, 47, 18, 100, 100, 86, 17, 15, 117, 27, 110, 56, 6, 69, 7,\
 47, 16, 63, 111, 2, 19, 9, 43, 94]

res = [0 for i in range(len(arr))]

for i in range(0, len(arr)):
	if i %3 == 0:
		res[i] = arr[i]^7
	elif i %3 == 1:
		res[i] = arr[i]^6
	else:
		res[i] = arr[i]^5
	if i % 2 == 0:
		res[i] ^= 9
	else:
		res[i]^= 8
	
	res[i]^= (i%10)
	if (i>2):
		res[i] = res[i]^arr[i-3]
	if i>0:
		res[i] = res[i]^arr[i - 1]
	res[i]^=20

for i in res:
	print(chr(i), end = '')
print()