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
for i in range(500,540):
	flag = remove(send_data(url,i))
	print flag.decode('hex')
	