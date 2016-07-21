import requests
import binascii
i=530
while (1):
	i+=1
	if (requests.post('https://shrouded-falls-79294.herokuapp.com', data = {'msg': '\0'*i}).content.replace(' ','') == '<h1>InternalServerError</h1>'):
		break
i-=1
r = requests.post('https://shrouded-falls-79294.herokuapp.com', data = {'msg': '\0'*i}).content.replace(' ','')
print r.decode("hex")