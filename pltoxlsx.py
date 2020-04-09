import pandas as pd
import requests
import re
import time

first = "https://movie.douban.com/subject/34805219/comments?start="
last = '&limit=20&sort=new_score&status=P'
data_list = []

for i in range(0, 200, 20):
    url = first + str(i) + last
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    }
    print('正在爬第%d页' % i)
    try:
        data = requests.get(url, headers=headers).text
        # time.sleep(5)
        result = re.findall('<span class="short">(.*?)</span>', data)
        data_list.extend(result)
    except:
        print("本页爬取失败")

df = pd.DataFrame()
df["评论"] = data_list
df.to_excel("评论_汇总%s.xlsx" % time.ctime())
