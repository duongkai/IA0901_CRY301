import urllib
import urllib2
import binascii
def send_data(url,key_length):
	zero_byte = '%00' * key_length
	data = 'msg=' + zero_byte
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	return the_page
def remove(string):
	string = string.replace(' ','')
	return string
# ========================================
url = 'https://shrouded-falls-79294.herokuapp.com/'	
i = 535
while True:
	try:
		send_data(url,i)
		i+=1
	except:
		key_length = i - 1 
		break
# print key_length
flag = remove(send_data(url,key_length))
print flag.decode('hex')


