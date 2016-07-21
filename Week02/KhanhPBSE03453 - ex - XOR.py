import requests

url = 'https://shrouded-falls-79294.herokuapp.com'

i=1

while (1):
	i=i+50
	if (requests.post(url, data = {'msg': '\x00'*i}).content.replace(' ','') == '<h1>InternalServerError</h1>'):
		i=i-50
		break

while (1):
	i=i+1
	if (requests.post(url, data = {'msg': '\x00'*i}).content.replace(' ','') == '<h1>InternalServerError</h1>'):
		break

i=i-1

r = requests.post(url, data = {'msg': '\x00'*i}).content.replace(' ','')

print r.decode("hex") 