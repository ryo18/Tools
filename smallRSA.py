# reference: https://en.wikipedia.org/wiki/Wiener%27s_attack

import math
e = 165528674684553774754161107952508373110624366523537426971950721796143115780129435315899759675151336726943047090419484833345443949104434072639959175019000332954933802344468968633829926100061874628202284567388558408274913523076548466524630414081156553457145524778651651092522168245814433643807177041677885126141
n = 380654536359671023755976891498668045392440824270475526144618987828344270045182740160077144588766610702530210398859909208327353118643014342338185873507801667054475298636689473117890228196755174002229463306397132008619636921625801645435089242900101841738546712222819150058222758938346094596787521134065656721069
c = 2729869850246221096831391096846794169956396740264942203903703342885290746934874117725386729017627214993949187059358671448548783102300956256114813913061908317052353475608677702004762353569798758999446296443701747957565699931341341707067812649227617863345146556649686184642966609793205244209896583560093620273
list1 = []
a = 0
b = 0
# find x + 1/ (y + 1/(...
while(1):
	a = n/e # ho~n so
	b = n%e # 
	list1.append(a)
	if b == 1:
		list1.append(e)
		break
   	n = e
	e = b

def iroot(k, n):
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s
    
e = 165528674684553774754161107952508373110624366523537426971950721796143115780129435315899759675151336726943047090419484833345443949104434072639959175019000332954933802344468968633829926100061874628202284567388558408274913523076548466524630414081156553457145524778651651092522168245814433643807177041677885126141
n = 380654536359671023755976891498668045392440824270475526144618987828344270045182740160077144588766610702530210398859909208327353118643014342338185873507801667054475298636689473117890228196755174002229463306397132008619636921625801645435089242900101841738546712222819150058222758938346094596787521134065656721069

# cong don 
def cal_sum(x,y,z):
	return x*y+z,y
list2 = []
list3 = []

# e/n = k/d
# lay limit tung so hang de co 1 phan so
# --> lay duoc tu so va mau so cua k/d
for i in range(len(list1)):
	j = i
	f = list1[j]
	c = 1
	while(j > 0):
		b = list1[j-1]
		f,c =  cal_sum(b,f,c)
		j-=1
	list2.append(f) # mau so
	list3.append(c) #tu so


d = 0

#find q,p,d 
for i in range(len(list2)):
	d = list2[i]
	k = list3[i]
	phi_n = (e*d - 1) / k
  # phuong trinh bac 2: x^2 - (n -phi_n + 1)*x + n = 0, nghiem la p,q
	a = 1
	b = n - phi_n + 1
	c = n
	delta = b*b - 4*a*c
	x = iroot(2,delta)
	p = (b + x)/(2)
	q = (b - x)/(2)
	if p*q == n:
		print p,q,d
		break

e = 165528674684553774754161107952508373110624366523537426971950721796143115780129435315899759675151336726943047090419484833345443949104434072639959175019000332954933802344468968633829926100061874628202284567388558408274913523076548466524630414081156553457145524778651651092522168245814433643807177041677885126141
n = 380654536359671023755976891498668045392440824270475526144618987828344270045182740160077144588766610702530210398859909208327353118643014342338185873507801667054475298636689473117890228196755174002229463306397132008619636921625801645435089242900101841738546712222819150058222758938346094596787521134065656721069
c = 2729869850246221096831391096846794169956396740264942203903703342885290746934874117725386729017627214993949187059358671448548783102300956256114813913061908317052353475608677702004762353569798758999446296443701747957565699931341341707067812649227617863345146556649686184642966609793205244209896583560093620273

m = pow(c,d,n)
data = hex(m)

print ''.join(chr(int(data[i:i+2],16)) for i in range(2,len(data)-1,2))

