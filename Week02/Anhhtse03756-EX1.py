import urllib
import urllib2
url = 'https://shrouded-falls-79294.herokuapp.com/'	
for i in range (530,540):
	byte_zero='%00' * i
	data = 'msg=' + byte_zero
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	flag = the_page.replace(' ','')
	print flag.decode('hex')