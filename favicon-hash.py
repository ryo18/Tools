import mmh3
import requests
import codecs

url = 'url/favicon.ico'
response = requests.get(url)
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print("[+] URL: "+ url + "\n[+] hash: " + str(hash))