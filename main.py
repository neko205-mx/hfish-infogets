import threading
import time
import requests
import json
import os
import socket
"""
    
"""

def getKeyAndip():
    # ip = ""
    # key = ""
    ip = os.getenv('URL')
    key = os.getenv('URLKEY')
    return ip,key
# 获取时间戳 当前时间点往前24小时
def timeStart():
    newday = time.time()
    # oldday = int(newday) - 86400
    oldday = int(newday) - 10 #测试用
    newday = int(newday)
    return oldday,newday
def main():
    user_input = input("选择所获取的数据：1 获取攻击数据 2 获取服务器状态")
    if user_input == "1":

        json_date = json.loads(apiGetHackip())
        if json_date['response_code'] == 0:
            print("获取成功")
            Hackips = json_date['data']['attack_ip']
            print(Hackips)
            CheckOpen = ipCheck(Hackips) # 调用
            print(CheckOpen)

            # print(json_date)
        else:
            print("获取失败")
            # print(json_date)
            
    elif user_input == "2":
        json_date = json.loads(apiGetServerStatus())
        print("获取服务器状态")

        if json_date['response_code'] == 0:
            print("获取成功")
            online_date = json_date['data']['total_online_honeypots']
            offine_date = json_date['data']['total_offline_honeypots']

            print("在线设备：" + str(online_date))
            print("离线设备：" + str(offine_date))
            if offine_date == 0:
                print("蜜罐运行正常")
            else:
                print("请检查离线蜜罐状态")

        else:
            print("获取失败")
            print(json_date)
    else:
        print("输入错误")

def ipCheck(Hackips):
    PortOpen = {}
    Port = [22,3306,6379,3389,1443,23]
    for i in Hackips:
        for p in Port:
            if PortScan(i,p):
                PortOpen[i] = p
                print(i + ":" + str(p) + "端口开放")
            else:
                print(i + ":" + str(p) + "端口未开放")
    return PortOpen


def PortScan(ip,port):

    socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socks.settimeout(1)
    try:
        socks.connect((ip, port))
        socks.close()
        return True
    except:
        return False
    

def apiGetHackip():
    ip,key = getKeyAndip()
    oldday,newday = timeStart()

    # 获取攻击数据
    url = f"https://{ip}/api/v1/attack/ip?api_key={key}"
    print(url)
    payload = json.dumps({
     "start_time": oldday,
     "end_time": newday,
     "intranet": 0,
     "threat_label": [
    
     ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    # 忽略证书验证
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    return response.text


def apiGetServerStatus():
    ip,key = getKeyAndip()
    # 获取服务器状态
    url = f"https://{ip}/api/v1/hfish/sys_info?api_key={key}"
    response = requests.request("GET", url, verify=False)
    return response.text


if __name__ == '__main__':
    main()