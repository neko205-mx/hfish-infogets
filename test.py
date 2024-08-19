import json
import socket

# JSON字符串
json_string = '''
{
    "response_code": 0,
    "verbose_msg": "成功",
    "data": {
        "attack_ip": [
            "1.1.1.1",
            "193.201.9.156",
            "205.210.31.144",
            "45.83.65.238",
            "172.70.86.15"
        ]
    }
}
'''

# 解析JSON字符串为Python字典
parsed_json = json.loads(json_string)

# 访问data字典中的attack_ip列表
attack_ips = parsed_json['data']['attack_ip']
attack_ips2 = parsed_json['response_code']
attack_ips3 = parsed_json['verbose_msg']

print(attack_ips,attack_ips2,attack_ips3)  # 输出: ['198.235.24.254', '193.201.9.156', '205.210.31.144', '45.83.65.238', '172.70.86.15']
print(type(attack_ips)) 



def check_port(ip, port):  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.settimeout(5)  
  
    try:  
        result = sock.connect_ex((ip, port))  
        if result == 0:  
            return True
        else:  
            return False
    except Exception as e:  
        print(f"错误: {str(e)}")  
    finally:  
        sock.close()



for ip in attack_ips:
    xx = check_port(ip, 12312)

    if xx == True:
        print(f"{ip} 端口12312开放")
    else:
        print(f"{ip} 端口12312未开放")
