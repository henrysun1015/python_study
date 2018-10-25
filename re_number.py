#-coding:utf-8-*-
import requests
import re
url = "http://ctf5.shiyanbar.com/jia/"
session = requests.Session()
res1 = session.get(url)
zhengze = r"'my_expr'>(.*)</div>"

res2 = re.findall(zhengze,str(res1.content,'gb2312'))[0]
list = re.sub('[()+x-]','',res2).split()    #将符号替换为空，之后将空格删除并放入列表
res3 = (int(list[0])+int(list[1]))*(int(list[2])-int(list[3]))-(int(list[4])+int(list[5])-int(list[6]))*int(list[7])
payload = {'pass_key':res3}
res4 = session.post(url+'index.php?action=check_pass',payload)
print(str(res4.content,'gb2312'))