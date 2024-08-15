import time
import requests
import json
import os
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
    oldday = int(newday) - 86400
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
            # print(json_date)
        else:
            print("获取失败")
            # print(json_date)
            
    elif user_input == "2":
        print("获取服务器状态")
    else:
        print("输入错误")


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

if __name__ == '__main__':
    main()