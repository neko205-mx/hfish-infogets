import time
import requests
import json

"""
    
"""

def getKeyAndip():
    ip = ""
    key = ""
    return ip,key
# 获取时间戳 当前时间点往前24小时
def timeStart():
    newday = time.time()
    oldday = int(newday) - 86400
    newday = int(newday)
    return oldday,newday
def main():
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
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    print(response.text)
    echo = response.text
    print(echo)

if __name__ == '__main__':
    main()