import sys
import time
import argparse
import textwrap
import threading
import subprocess
import json
from ipaddress import ip_address
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

def get_port_list(number, ip_str, show_time):
    ip_str = (ip_str).split('-')
    if len(ip_str) == 1:
        ip_str = ip_str[0]
    elif len(ip_str) == 2:
        print('暂时只支持扫描单个IP')
        sys.exit(1)
    IP_QUEUE = Queue()  # 创建一个队列
    port_result = dict()
    for port in range(1,1025):
        IP_QUEUE.put([ip_str,port])  # 将ip，port写入队列中

    def scan_port(ip_port):
        ip = str(ip_port[0])
        port = str(ip_port[1])
        try:
            res = subprocess.call('nc -z -w1 %s %s' % (ip, port), stdout=subprocess.PIPE,
                                  shell=True)  # MAC上的nc命令，其它操作系统根据操作系统调整
        except Exception as e:
            print("扫描端口报错 %s" % str(e))
        # 打印运行结果
        print(port, True if res == 0 else False)
        if lock.acquire():
            if res == 0:
                port_result[port] = 'Open'
            else:
                port_result[port] = 'Close'
            lock.release()

    # 根据用户指定的线程池个数创建线程池
    pool = ThreadPoolExecutor(max_workers=number)
    lock = threading.Lock()
    start_time = time.time()
    all_task = []
    while not IP_QUEUE.empty():
        all_task.append(pool.submit(scan_port, IP_QUEUE.get()))
    # 等待所有任务结束
    wait(all_task, return_when=ALL_COMPLETED)
    if show_time:
        print('scan耗时：%s' % (time.time() - start_time))
    return port_result


def get_ip_list(number, ip_str, show_time):
    ip_str = (ip_str).split('-')
    if len(ip_str) == 1:
        ip_start = ip_str[0]
        ip_end = ip_str[0]
    elif len(ip_str) == 2:
        ip_start = ip_str[0]
        ip_end = ip_str[1]
    IP_QUEUE = Queue()    #创建一个队列
    ip_result = dict()
    ip_start = ip_address(ip_start)
    ip_end = ip_address(ip_end)
    while ip_start <= ip_end:
        IP_QUEUE.put(str(ip_start))  #将ip写入队列中
        ip_start += 1

    def ping_ip(ip):
        try:
            res = subprocess.call('ping -c 2 -t 3 %s' % ip, stdout=subprocess.PIPE, shell=True)  #MAC上的ping命令，其它操作系统根据操作系统调整
        except Exception as e:
            print("ping主机报错 %s" % str(e))
        # 打印运行结果
        print(ip, True if res == 0 else False)
        if lock.acquire():
            if res == 0:
                ip_result[ip] = 'True'
            else:
                ip_result[ip] = 'False'
            lock.release()

    # 根据用户指定的线程池个数创建线程池
    pool = ThreadPoolExecutor(max_workers=number)
    lock = threading.Lock()
    start_time = time.time()
    all_task = []
    while not IP_QUEUE.empty():
        all_task.append(pool.submit(ping_ip, IP_QUEUE.get()))
    # 等待所有任务结束
    wait(all_task, return_when=ALL_COMPLETED)
    if show_time:
        print('ping耗时：%s' % (time.time() - start_time))
    return ip_result




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent("""\
            Host scan tools
    
            ===Example Usage===
            python3 pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100
            python3 pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json
            ===================
    
            """)
    )
    parser.add_argument("-n", required=False, default="4", type=int, help="Concurrent number")
    parser.add_argument("-f", help="Use ping or tcp")
    parser.add_argument("-ip", required=False, default="127.0.0.1", type=str, help="Use ip or ip segment")
    parser.add_argument("-w", required=False, default=None, help="Save to file")
    parser.add_argument('-v', action='store_true', help='show elapsed time')
    args = parser.parse_args(sys.argv[1:])
    if args.f == 'ping':
        scan_result = get_ip_list(args.n, args.ip, args.v)
    elif args.f == 'tcp':
        scan_result = get_port_list(args.n, args.ip, args.v)
    if args.w:
        result_json = json.dumps(scan_result)
        file_name = args.w
        try:
            with open(file_name, 'w', encoding='utf-8') as json_file:
                json_file.write(result_json)
        except IOError as e:
            print('File Error:' + str(e))
        else:
            print("扫描结果操作到 %s 成功" % file_name)

