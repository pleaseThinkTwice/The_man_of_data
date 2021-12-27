# -*- coding: UTF-8 -*-
import random
import time

import requests
import xlsxwriter
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

import json
def ini_cell():
    l2=["id",'name','channel_count','id','name','subscribed_count','archive_count','featured_count']
    l1=["19大类每个类的id","19类每个类的名字","每个大类分为多少个小类","每个小类的id","每个小类的名","每个小类的订阅数","每个小类的视频总数"]
    return l1,l2
def main ():
    baseurl = "https://api.bilibili.com/x/web-interface/web/channel/category/channel_arc/list?id="
    categories=nineteen()
    workbook = xlsxwriter.Workbook("19categories.xls")
    worksheet = workbook.add_worksheet('sheet1')
    l1,l2=ini_cell()
    worksheet.write_row('A1', l1)
    worksheet.write_row('A2', l2)
    n=3
    try:
        for i in range(2,len(categories)):
            info1=[categories[i]['id'],categories[i]["name"],categories[i]["channel_count"]]
            baseurl2=baseurl+str(categories[i]["id"])
            for j in range(0,int(categories[i]['channel_count']),6):
                baseurl3=baseurl2+"&offset="+str(j)
                # print(baseurl3)
                data=getData(baseurl3)
                time.sleep(0.7 + 0.5 * random.random())
                for k in data["data"]["archive_channels"]:

                    info2=[k['id'],k['name'],k['subscribed_count'],k['archive_count']]
                    info=info1+info2
                    print(info)
                    worksheet.write_row('A' + str(n), info)
                    n=n+1
    except Exception as result:
        print("出错", result)
    finally:
        workbook.close()
    exit()
def nineteen():
    baseurl = "https://api.bilibili.com/x/web-interface/web/channel/category/list"
    data = getData(baseurl)["data"]
    categories=data["categories"]
    detail=[categories[i] for i in range(len(categories))]
    return detail
def getData(baserul):
    url = baserul
    html = askURL(url)
    json_str = html
    user_dic = json.loads(json_str)
    return user_dic
def askURL(url):
    # 模拟浏览器
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
    request= urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
if __name__ == "__main__":
    main()