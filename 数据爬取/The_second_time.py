import random
import time
import xlsxwriter
from bs4 import BeautifulSoup
import requests
import re
findNumber = re.compile(r"\d*")
def T():
    return (1+random.random())*2
# 初始化 x y 坐标
import threading
def ini_cell():
    l1 = ["mid","media_count"]
    l2 = ["用户的id","用户收藏的视频总数"]
    return l2, l1


def random_consecutive_number_list(m, n, step):
    # random.shuffle(consecutive_number_list)
    return [i for i in range(m,n+1)]


def go(excel_name,begin,end):

    workbook = xlsxwriter.Workbook(excel_name)  # 新建excel表
    worksheet = workbook.add_worksheet('sheet1')
    l1, l2 = ini_cell()
    worksheet.write_row('A1', l1)
    worksheet.write_row('A2', l2)
    n = 3
    uid_list = random_consecutive_number_list(begin, end, 1)
    print("随机列表生成成功")
    # print(uid_list)
    # exit()
    try:
        for i in uid_list:
            try:
                print(i)
                time.sleep(T())
                user_information = media_count(i)
                worksheet.write_row('A' + str(n), [i,user_information])
                n = n + 1
                # print("user信息提取成功")
            except Exception as result:
                print("第二个循环出错", result)
            finally:
                pass
    except Exception as result:
        print("第一个循环出错",result)
    finally:
        workbook.close()
    exit()
def head():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)
    headers = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                        '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                       )
    return {"User-Agent":headers}
def get_uid_url(uid):
    url = "https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid=" + str(uid) + "&jsonp=jsonp"
    # print(url)
    # https://api.bilibili.com/x/v3/fav/folder/created/list-all?up_mid=17&jsonp=jsonp
    return url
def askUrl_normal_json(uid):

    # 返回收藏夹的信息
    time.sleep(T())
    headers = head()
    url = get_uid_url(uid)
    response = requests.get(url=url, headers=headers, timeout=T())
    normal_json = response.json()
    time.sleep(T())
    return normal_json
def media_count(uid):
    normal_json = askUrl_normal_json(uid)
    media_count = 0
    if normal_json["data"] == None:
        return media_count
    else:
        for i in range(len(normal_json["data"]["list"])):
            media_count+=normal_json["data"]["list"][i]["media_count"]
    return media_count


class myThread (threading.Thread):
    def __init__(self, threadID, name,excel_name,begin,end):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.excel_name=excel_name
        self.begin=begin
        self.end = end
    def run(self):
        print ("开始线程：" + self.name)
        go(self.excel_name,self.begin,self.end)
        print ("退出线程：" + self.name)
start = time.time()
# 1.37975
# 2.8279
num_of_thread=30 #多少个线程
mul = 3206# 一个线程多少个uid
begin=3840 #爬虫的起点 从哪个用户开始爬
threadID=[i for i in range(num_of_thread)]
# 生成多少个线程以及线程的id
thread_name=['thread'+str(i) for i in threadID]
# 每个线程的名字
excel_name=[str(begin+i*mul)+"_"+str(begin+(i+1)*mul-1)+".xlsx" for i in threadID]
# 每个excel的名字
thread_list=[]
for i in range(len(threadID)):
    thread_list.append(myThread(threadID[i],thread_name[i],excel_name[i],begin+i*mul,begin+(i+1)*mul-1))
    # 后面两个数字参数是起点和终点
#     初始化每个线程
for i in range(len(threadID)):
    thread_list[i].start()
    time.sleep(T())
#     开始线程
for i in range(len(threadID)):
    thread_list[i].join()
    time.sleep(T())
#     一起跑
end = time.time()
print(end - start)