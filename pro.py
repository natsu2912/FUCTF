from pwn import *
import sys

def wf(fn, x):
	f = open(fn, 'a')
	f.write(x)
	f.close()

path = "/home/ctf/maze"

s = remote('139.180.213.85', 10005)
print s.recvuntil('Enter choice: \n')
s.sendline('1')
print '1'
print s.recvuntil('\n')
s.sendline(path)
print path
a = s.recvuntil('\n')
print a
a = a[2:len(a)-3]
a = a.split("', '")
s.close()

for i in range(4): #+omez
	temp = path +'/'+ a[i]
	s = remote('139.180.213.85', 10005)
	print s.recvuntil('Enter choice: \n')
	s.sendline('1')
	print '1'
	print s.recvuntil('\n')
	s.sendline(temp)
	print temp
	b = s.recvuntil('\n')
	print b
	b = b[2:len(b)-3]
	b = b.split("', '")
	s.close()

	for j in range(4): #+ahlr
		temp = path +'/'+ a[i] +'/'+ b[j]
		s = remote('139.180.213.85', 10005)
		print s.recvuntil('Enter choice: \n')
		s.sendline('1')
		print '1'
		print s.recvuntil('\n')
		s.sendline(temp)
		print temp
		c = s.recvuntil('\n')
		print c
		c = c[2:len(c)-3]
		c = c.split("', '")
		s.close()

		for k in range(4): #+tcqt
			temp = path +'/'+ a[i] +'/'+ b[j] +'/'+ c[k]
			s = remote('139.180.213.85', 10005)
			print s.recvuntil('Enter choice: \n')
			s.sendline('1')
			print '1'
			print s.recvuntil('\n')
			s.sendline(temp)
			print temp
			d = s.recvuntil('\n')
			print d
			d = d[2:len(d)-3]
			d = d.split("', '")
			s.close()

			for l in range(4): #+jklu
				temp = path +'/'+ a[i] +'/'+ b[j] +'/'+ c[k] +'/'+ d[l]
				s = remote('139.180.213.85', 10005)
				print s.recvuntil('Enter choice: \n')
				s.sendline('1')
				print '1'
				print s.recvuntil('\n')
				s.sendline(temp)
				print temp
				e = s.recvuntil('\n')
				print e
				e = e[2:len(e)-3]
				e = e.split("', '")
				s.close()

				for m in range(4): #+udjk
					temp = path +'/'+ a[i] +'/'+ b[j] +'/'+ c[k] +'/'+ d[l] +'/'+ e[m]
					s = remote('139.180.213.85', 10005)
					print s.recvuntil('Enter choice: \n')
					s.sendline('1')
					print '1'
					print s.recvuntil('\n')
					s.sendline(temp)
					print temp
					f = s.recvuntil('\n')
					print f
					f = f[2:len(f)-3]
					s.close()

					temp = path +'/'+ a[i] +'/'+ b[j] +'/'+ c[k] +'/'+ d[l] +'/'+ e[m] +'/'+ f
					s = remote('139.180.213.85', 10005)
					print s.recvuntil('Enter choice: \n')
					s.sendline('1')
					print '1'
					print s.recvuntil('\n')
					s.sendline(temp)
					print temp
					g = s.recvuntil('\n')
					print g
					if g == '[]\n':
						wf('fail', temp + g)
					else:
						wf('success', temp + g)			
						sys.exit()
