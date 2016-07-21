import requests

url = 'https://shrouded-falls-79294.herokuapp.com'
i = 530
backup = ''
while True:
	data = dict(msg = '\x00' * i)
	i += 1
	r = requests.post(url, data=data)
	if (r.content == '<h1>Internal Server Error</h1>'): 
		break
	backup = r.content

backup =  backup.replace(' ','')
print backup.decode('hex')
