import requests
import binascii
import re
def getFlag(key_length,k):
	try:
		payload =  "\0"*key_length
		r = requests.post('https://shrouded-falls-79294.herokuapp.com/', data={'msg':payload})
		print "[+] Checking key length",key_length
		pattern = re.compile(ur'flag{.+}')
		flag = re.search(pattern,binascii.unhexlify(''.join(r.text.split())) )
		if flag:
			print "FLAG found!"
			print flag.group(0) 
		else:
			key_length = key_length + k
			getFlag(key_length,k)
	except:
		k = k/2
		key_length = key_length - k		
		getFlag(key_length,k)

if __name__ == "__main__":
	getFlag(0,100)

