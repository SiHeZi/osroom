# -*-coding:utf-8-*-
import socket

import pwd

import os

__author__ = "Allen Woo"

def get_host_info(ifname='eth0'):

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
    except Exception as e:
        local_ip = None
    finally:
        s.close()
    try:
        username = pwd.getpwuid(os.getuid())[0]
    except:
        username = ""
    hostname = socket.gethostname()
    host_info = {"local_ip":local_ip, "hostname":hostname, "username":username}

    # 资源使用情况

    resource = {"mem_used_per":None, "cpu_used_per":None, "mem_free":None}
    try:
        import psutil
        mem = psutil.virtual_memory()
        resource["mem_total"] = mem.total
        resource["mem_used"] = mem.used
        resource["mem_free"] = mem.free
        resource["mem_used_per"] = float('%.2f'%(resource["mem_used"]/float(resource["mem_total"])))
        resource["cpu_used_per"] = psutil.cpu_percent()*0.01
    except:
        pass
    host_info["resource"] = resource
    return host_info