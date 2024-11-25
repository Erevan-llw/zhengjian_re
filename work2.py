import re
import requests

url = 'http://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/ZYZBAjaxNew?type=1&code=SH600062'
resp = requests.get(url)
fileName = 'file.html'
with open(fileName, 'w', encoding='utf_8') as fp:
    fp.write(resp.text)
    print(fileName, "保存成功！")
obj = re.compile(r'"ROEJQ" : (?P<ROE>.*?),', re.S)
result = obj.finditer(resp.text)
for it in result:
    dic = it.groupdict()
    print(dic.values())

# 注意，仅实现了单个数据（ROE）的逐年爬取，由于项目内已有完备的数据库，所以只是制作了较为简略的demo，需要更多数据可以在file.html内进行进一步挑选
