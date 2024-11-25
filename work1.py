import csv

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
f = open('list_file.csv', mode='w', encoding='utf-8', newline='')
csv_write = csv.writer(f)
csv_write.writerow(['上市编号', '上市公司名', '违纪类型', '红头文件'])
# pageHelp.pageNo/pageHelp.beginPage/pageHelp.endPage
url = 'http://www.sse.com.cn/disclosure/credibility/supervision/measures/?query=pageHelp.pageNo=2'
driver.get(url)
driver.implicitly_wait(10)
i = 0
while i < 133:
    trs = driver.find_elements(By.XPATH, '/html/body/div[8]/div/div[2]/div/div[1]/div[1]/table/tbody/tr')
    for tr in trs:
        number = tr.find_element(By.XPATH, 'td[1]/span').text
        name = tr.find_element(By.XPATH, 'td[2]/span').text
        _class = tr.find_element(By.XPATH, 'td[3]').text
        if _class == '监管警示' or _class == '通报批评' or _class == '公开认定' or _class == '公开谴责':
            url_temp = tr.find_element(By.XPATH, 'td[4]/a')
            _text = url_temp.get_attribute('href')
        else:
            _text = 'NO SUCH FILE!'
        print(number, name, _class, _text)
        csv_write.writerow([number, name, _class, _text])
    driver.find_element(By.XPATH, '/html/body/div[8]/div/div[2]/div/div[1]/div[2]/ul/li[9]').click()
    print(f'第{i+1}页完成！')
    i = i + 1
f.close()
print("over!")
