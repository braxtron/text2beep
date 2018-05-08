import sys

i = 1
beepStr = ''
while i < len(sys.argv[1]):
	if sys.argv[1][i] == 'e':
		beepStr += '1'
	else:
		beepStr += '0'
	i += 4
n = int(beepStr, 2)
print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())