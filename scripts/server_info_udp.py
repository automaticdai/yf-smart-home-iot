#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, time, socket
from collections import OrderedDict

UDP_IP = "127.0.0.1"
UDP_PORT = 8888

def load_stat(): 
    loadavg = {} 
    f = open("/proc/loadavg") 
    con = f.read().split() 
    f.close() 
    loadavg['lavg_1']=con[0] 
    loadavg['lavg_5']=con[1] 
    loadavg['lavg_15']=con[2] 
    loadavg['nr']=con[3] 
    loadavg['last_pid']=con[4] 
    return loadavg 

def mem_getinfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo



if __name__=='__main__':
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((socket.gethostname(), UDP_PORT))
	
	while (True):
		data, addr = sock.recvfrom(1024)
		print "received request from " , addr, ":", data

		reply_msg = ""
		lavg = load_stat()
		reply_msg = reply_msg + "CPU Load (1 min): {0}\r\n".format(lavg['lavg_1'])
		reply_msg = reply_msg + "CPU Load (5 mins): {0}\r\n".format(lavg['lavg_5'])
		reply_msg = reply_msg + "CPU Load (15 mins): {0}\r\n".format(lavg['lavg_15'])

		meminfo = mem_getinfo()
		reply_msg = reply_msg + 'Total memory: {0}\r\n'.format(meminfo['MemTotal'])
		reply_msg = reply_msg + 'Free memory: {0}\r\n'.format(meminfo['MemAvailable'])
		sock.sendto(reply_msg, addr)
	
	sock.close()
