import re
import requests
import base64
import io
import sys
r = requests.Session()#因为reqests请求的和post提交的数据要保持一致
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')#改变默认输出的编码
html = r.head('http://ctf5.shiyanbar.com/web/10/10.php')
result = html.headers
results = result['FLAG']
print(results)
de_results = str(base64.b64decode(results.encode('utf-8')),'utf-8')
print(de_results)
data = de_results.split(':',1)[1]
print(data)
flag = {'key':data}
flags = r.post('http://ctf5.shiyanbar.com/web/10/10.php', data=flag)
print(flags.text)