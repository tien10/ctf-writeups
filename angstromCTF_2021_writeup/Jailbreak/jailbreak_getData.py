from struct import unpack
from idc import GetManyBytes


def GetData(dataAddress, dataSize, dataNum):
	data = []
	for i in xrange(0, dataNum*dataSize, dataSize):
		dataByte = GetManyBytes(dataAddress + i, dataSize)
		if dataSize == 1:
			data.append(unpack('B', dataByte)[0])
		elif dataSize == 4:
			data.append(unpack('I', dataByte)[0])
	return data

def sub_15a0(arr0, BigArr, a1):
	v1 = arr0[a1]
	v2 = arr0[a1 + 1] - v1
	retStr = ''
	if v2 > 0:
		i = 0
		v5 = a1
		while i != v2:
			v7 = (v5 ^ BigArr[v1 + i])&0xff
			retStr += chr(v7) 
			i+=1
			v5 = (v5*v7 + 17*a1)&0xffffffff
	return retStr


def main():
	arr0 = GetData(0x4080, 4, 32)
	BigArr = GetData(0x4100, 0x1, 1599)
	a1 = [i for i in xrange(len(arr0) - 1)]
	
	for i in xrange(0, len(a1)):
		arr = sub_15a0(arr0, BigArr, i)
		print str(i) + " " +arr
main()