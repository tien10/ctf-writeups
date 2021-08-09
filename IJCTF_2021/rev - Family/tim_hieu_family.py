'''
cnt == -1

eax = 0x1337
ebx = 0x8049548
edx = 0x080494B9




loc_80494B9:            # LOOP_BODY
case eax = 0x55555555:
	cnt++
case eax = 0x33333333:
	edx = arr1[cnt]  			# mảng arr1 nằm tại 0x804A060
lodsb
mov     bl, al

case eax = 0x69696969:
	eax = (ebx ^ edx)&0xff
mov     bl, al

case eax = 0x22222222:
	edx = arr2[cnt]				# mảng arr2 nằm tại 0x804A020

case eax = 0xF0F0F0F0:
	eax = (ebx + edx)&0xff
mov     bl, al

case eax = 0x11111111:
	edx = arr3[cnt]				# mảng arr3 nằm tại 0x804A0A0

case eax = 0xFEFEFEFE:
	eax = (ebx + edx)&0xff
mov     bl, al

case eax = 0x44444444:
	edx = arr4[cnt]				# mảng arr4 nằm tại 0x804A0E0 
cmp     bl, dl




'''



arr_804A060 = bytearray.fromhex('3A F7 00 68 06 2E 29 89  F4 67 2E C6 D6 6E 12 751B BA 64 44 1B 24 A5 30  3A FE A7 0D 74 AF 99 CE12 E1 1A 92 87 F3 DD DD  F3')
arr_804A060 = list(arr_804A060)
arr_804A020 = bytearray.fromhex('BB F0 D9 F2 28 63 A1 93  92 C5 35 EE 47 9A 5E 8626 D7 D5 52 B0 64 92 E3  E8 4C 82 A4 B8 9F 9A C0A8 CE 10 7A E3 BF C7 D5  3B')
arr_804A020 = list(arr_804A020)
arr_804A0A0 = bytearray.fromhex('C9 06 A4 4E 5D 33 CB E7  CA B3 77 E3 64 0C 8B C8EE 14 A2 70 42 89 BF E2  22 1A B9 F5 9A 71 B2 BA3C 3E 6D AF BD 0A 1D 82  64 ')
arr_804A0A0 = list(arr_804A0A0)
arr_804A0E0 = bytearray.fromhex('65 A7 78 E0 0B 85 34 8D  55 4A 08 BA 95 BF 4E E8B7 98 6E 12 E1 28 A9 70  D3 D1 8B 1E 2F F9 97 01E0 15 1E 71 E4 77 68 11  65')
arr_804A0E0 = list(arr_804A0E0)



for i in range(0, len(arr_804A0A0)):
	for ch in range(33, 126):
		bl = ch
		bl = (bl ^ arr_804A060[i]) & 0xff
		bl = (bl + arr_804A020[i]) & 0xff
		bl = (bl - arr_804A0A0[i]) & 0xff
		if bl == arr_804A0E0[i]:
			print(chr(ch), end = '')
			break
#IJCTF{why_did_i_do_this_7aebed65fda491cc}