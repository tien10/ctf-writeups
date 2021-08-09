mazeData = [[0, 0, 0, 0, 0, 0, 0, 0], [119, 223, 119, 255, 253, 255, 127, 253], [21, 81, 80, 80, 4, 17, 4, 21], [85, 117, 95, 87, 221, 245, 245, 213], [81, 5, 65, 20, 81, 4, 17, 85], [95, 125, 221, 215, 95, 119, 223, 119], [64, 68, 20, 81, 65, 81, 0, 1], [119, 223, 245, 223, 119, 93, 255, 247], [69, 0, 5, 0, 20, 68, 17, 4], [93, 223, 221, 127, 213, 215, 221, 247], [80, 80, 65, 64, 81, 16, 64, 17], [119, 223, 119, 93, 223, 245, 223, 215], [68, 1, 20, 81, 0, 21, 16, 84], [117, 253, 93, 223, 255, 221, 119, 247], [21, 5, 65, 16, 0, 65, 16, 1], [117, 119, 127, 127, 127, 95, 119, 253], [69, 80, 16, 0, 65, 80, 68, 21], [93, 215, 247, 255, 221, 93, 253, 213], [80, 20, 84, 0, 21, 69, 1, 81], [93, 245, 85, 255, 119, 125, 223, 95], [69, 5, 68, 80, 80, 0, 16, 80], [87, 127, 127, 215, 215, 255, 119, 223], [80, 64, 1, 4, 20, 1, 68, 1], [95, 215, 247, 125, 215, 119, 93, 215], [68, 20, 20, 64, 81, 84, 81, 84], [119, 247, 215, 95, 213, 215, 223, 85], [16, 16, 81, 84, 21, 4, 4, 85], [87, 215, 93, 85, 221, 117, 245, 223], [84, 81, 68, 81, 69, 81, 17, 64], [85, 223, 95, 215, 117, 95, 93, 95], [85, 0, 64, 20, 69, 64, 69, 17], [93, 255, 93, 255, 125, 125, 221, 247], [64, 1, 84, 0, 5, 5, 80, 21], [127, 127, 119, 253, 245, 93, 95, 213], [69, 64, 64, 5, 21, 81, 0, 85], [117, 119, 127, 119, 117, 215, 253, 213], [20, 21, 1, 81, 64, 84, 65, 21], [87, 117, 247, 93, 127, 87, 127, 117], [81, 68, 20, 68, 5, 81, 0, 20], [93, 95, 93, 223, 117, 215, 127, 215], [81, 65, 65, 1, 80, 20, 64, 81], [87, 119, 223, 125, 223, 117, 223, 215], [84, 16, 80, 80, 1, 68, 68, 5], [87, 223, 95, 95, 223, 119, 119, 245], [81, 65, 1, 5, 16, 81, 16, 21], [85, 93, 253, 245, 119, 221, 119, 221], [85, 20, 4, 17, 64, 5, 64, 65], [117, 247, 245, 247, 127, 125, 93, 221], [68, 4, 5, 5, 1, 65, 85, 21], [125, 245, 247, 125, 253, 221, 215, 119], [4, 69, 16, 64, 4, 16, 17, 64], [93, 221, 93, 245, 247, 223, 247, 125], [81, 85, 81, 21, 17, 16, 64, 5], [87, 85, 223, 117, 93, 119, 127, 245], [85, 16, 64, 69, 69, 68, 1, 21], [93, 127, 95, 95, 221, 93, 255, 85], [80, 68, 80, 64, 21, 69, 16, 85], [119, 93, 223, 93, 245, 125, 119, 85], [69, 81, 17, 85, 1, 5, 69, 85], [85, 221, 215, 117, 255, 125, 93, 117], [85, 4, 68, 5, 4, 65, 17, 5], [85, 119, 119, 245, 117, 221, 215, 119], [84, 80, 17, 20, 81, 20, 84, 81], [119, 223, 255, 119, 223, 247, 119, 223], [0, 0, 0, 0, 0, 0, 0, 0]]

def getMazeArray(mazeArray):
	for row in range(0, len(mazeData)):
		rowi = []
		for col in range(0, len(mazeData[row])):
			s = str(bin(mazeData[row][col])[2:]).rjust(8, '0')
			col = [int(i) for i in s]
			rowi.extend(col)
		rowi.extend([0])
		mazeArray.extend(rowi)
	return mazeArray

def getMaze(mazeArray):

	for row in range(0, 65):
		for col in range(0, 65):
			if row == 63 and col == 63:
				print('\033[1;32;40mFI', end = '')
			elif row == 1 and col == 1:
				print('\033[1;32;40mEN', end = '')
			else:
				if mazeArray[65*row + col] == 0:
					print('\033[1;34;40mxx', end = '')
				elif mazeArray[65*row + col] == 1:
					print('\033[1;33;40m  ', end = '')
				
		print()

#right: 0 --> tang 2 o
#down : 1 --> tang 130
#left : giam 2
#
#duyệt theo DFS dường như bị tràn stack hay gì á: RecursionError: maximum recursion depth exceeded in comparison

#def getNextNode(curNode):

offsets = {0: [2,0], 1: [0, 2], 2: [-2, 0], 3: [0, -2]}

def solve(curPos, preMove, path):
	if curPos[0] == 63 and curPos[1] ==63:
		#check = 1
		return True
	if preMove[-1] != 2 and mazeArray[65*curPos[1] + curPos[0] + 1] == 1 and mazeArray[65*curPos[1] + curPos[0] + 2] == 1:
		if solve([curPos[0] + 2, curPos[1]], preMove + [0], path):
			path.insert(0, 0)
			return True

	# go down

	if preMove[-1] != 3 and  mazeArray[65*(curPos[1] + 1) + curPos[0]] == 1 and mazeArray[65*(curPos[1]+2) + curPos[0]] == 1:
		if solve([curPos[0], curPos[1] + 2], preMove + [1], path):
			path.insert(0, 1)
			return True


	#go left: 2
	if preMove[-1] != 0 and  mazeArray[65*curPos[1] + curPos[0] - 1] == 1 and mazeArray[65*curPos[1] + curPos[0] - 2] == 1:
		if solve([curPos[0] -2, curPos[1]], preMove+ [2],path):
			path.insert(0,2)
			return True


	#go up
	if preMove[-1] != 1 and mazeArray[65*(curPos[1] - 1) + curPos[0]] == 1 and mazeArray[65*(curPos[1] - 2) + curPos[0]] == 1:
		if solve([curPos[0], curPos[1] - 2], preMove + [3], path):
			path.insert(0, 3)
			return True

	return False


def getOriBitArray(path):
	preMove = 0
	s = ''
	for move in path:
		if move - preMove == 1 or (preMove == 3 and move == 0):
			s += '11'
		elif move - preMove == -1 or (preMove == 0 and move == 3):
			s += '10'
		else:
			s += '0'
		preMove = move
	return s

if __name__ == '__main__':
	mazeArray = []
	#print(len(mazeData))
	mazeArray = getMazeArray(mazeArray)
	getMaze(mazeArray)

	maze = ', '.join(str(i) for i in mazeArray)
	open('maze.txt', 'w').write(maze)

	#for i in solve():
	path = []
	preMove = [0]
	solve([1,1], preMove, path)

	cipher = '0' + getOriBitArray(path)		#+ thêm '0' cho premove đầu tiên là 0
	key = '4E F7 68 21 D7 07 82 F9  DC 9D E6 B2 0A C2 F9 CBB4 D1 DC ED DB 17 2B 4B  35 F4 31 E7 E6 B2 12 8AA7 33 33 DA 8F 80 23 D4  1F 2C 04 13 D7 F6 D2 1EAE 1C C2 87 E3 70'
	key = bytearray.fromhex(key)
	ciphertext = [int(cipher[i:i +8], 2) for i in range(0, len(cipher), 8)]

	flag = ''.join(chr(int(ciphertext[i]) ^ key[i %len(key)]) for i in range(0, len(ciphertext)))
	print(flag)

