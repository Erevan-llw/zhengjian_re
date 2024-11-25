import pdfplumber
import pdfminer
import os
import wget
import csv
from collections import *

filename = 'list_file.csv'
# content = csv.reader(open(filename, 'r', encoding='utf-8'))
content = namedtuple('content', 'code,name,type,url')
_type = ['NO SUCH FILE!', '.shtml', '.pdf']
url_cast = []
for row in map(content._make, csv.reader(open(filename, 'r', encoding='utf-8'))):
    if _type[2] in row.url:
        # 以pdf形式存在的文件
        if row.url not in url_cast:
            wget.download(url=row.url, out=f'_file_pdf/{row.code}.pdf')
            print(row.url)
            url_cast.append(row.url)
    elif _type[1] in row.url:
        pass
    else:
        pass


