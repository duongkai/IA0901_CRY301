import requests
import binascii
i = 530
while(1):
	payload =  "\0"*i
	r = requests.post('https://shrouded-falls-79294.herokuapp.com/', data={'msg':payload})
	i+=1
	#print "\nRaw Data:", r.text
	if r.status_code == 500:
		break
	print "\nFlag:",binascii.unhexlify(''.join(r.text.split()))	
	
