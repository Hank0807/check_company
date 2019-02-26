import urllib.request as request
import json
from fuzzywuzzy import fuzz

# 台大網站
# url = 'https://www.ntu.edu.tw'

# 「臺北市內湖科技園區廠商名錄」API
url = 'https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c'

# 串接 API
with request.urlopen(url) as response:
    # data = response.read().decode('utf-8')

    # 利用 json 模組處理
    data = json.load(response)

# 一般網頁印出該網頁原始碼、API 印出 JSON 資料
# print(data['result']['results'])
myList = data['result']['results']

# 寫入檔案
with open('data.txt', 'w', encoding='utf-8') as file:
    for item in myList:
        file.write(item['公司名稱']+'\n')

# 讀取檔案
company_name = []

while True:
    keyin = input('請輸入要查詢的公司名稱:')
    with open('data.txt', 'r', encoding='utf-8') as file:
        # file_data = file.read() # 全部讀取
        if keyin == 'q':
            break
        for line in file:  # 一行一行讀取
            company_name.append(line.replace('\n', ''))
            result = fuzz.partial_ratio(keyin, line)
            #print ('result = ', result)
            if result == 100:
                print ('查詢結果 = ', line)
# print(file_data)
# print(company_name)

print ('Bye!')