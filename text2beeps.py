import sys

def str2bin(str):
	binStr = bin(int.from_bytes(str.encode(), 'big'))
	binStr = binStr[2:]
	while len(binStr) %8 != 0:
		binStr = '0' + binStr
	return binStr
	
def bin2beep(str):
	i = 0
	beepStr = ''
	while i < len(str):
		if str[i] == '1':
			beepStr += 'beep'
		else:
			beepStr += 'boop'
		i += 1
	return beepStr
		
binText = ''
i = 1
while i < len(sys.argv):
	binText += str2bin(sys.argv[i])
	binText += '00100000'
	i += 1

print(bin2beep(binText))

