#!/usr/bin/python
from binascii import unhexlify as uu

import requests

cc = 1
i = 1
url = "https://shrouded-falls-79294.herokuapp.com/"

while cc == 1:
	pp = requests.post(url,data={'msg' : '\x00'*i})
	if pp.status_code == 200:
		i = i + 20
		print i
		print pp.status_code
	else:
		cc = 0
		print i
		break

for j in range (i-20,i):
	while cc == 0:
		pp = requests.post(url,data={'msg' : '\x00'*j})
		if pp.status_code == 200:
			j = j + 1
			print j
			print pp.status_code
		else:
			cc = 1
			print (j-1)
			i=j-1
			break


pp1 = requests.post(url,data={'msg' : '\x00'*i})
tt1 = pp1.text

pp2 = requests.post(url,data={'msg' : '\x00'*i})
tt2 = pp2.text

ss1 = tt1.split()
ss2 = tt2.split()

ff=''
for v in range (0,len(ss2)):
	tt+=ss2[v].decode("hex")

for k in range(0, i):
	if ss1[k] == ss2[k]:
		ff += uu(ss1[k])
		k = k + 1
	else:
		ff=''
		k = k + 1
		
print ff
	


