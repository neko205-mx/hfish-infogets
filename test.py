import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

# 创建线程
for x in range(5):
    thread = threading.Thread(target=print_numbers,args=(ip, port_queue, open_ports))
    thread.start()
# 启动线程

# 等待线程结束
thread.join()