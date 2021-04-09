#!/usr/bin/python  
 
import os 

def load_stat(): 
    loadavg = {} 
    with open("/proc/loadavg") as f:
    	con = f.read().split()
    	loadavg['lavg_1'] = con[0] 
   	loadavg['lavg_5'] = con[1] 
    	loadavg['lavg_15'] = con[2] 
    	loadavg['nr'] = con[3] 
    	loadavg['last_pid'] = con[4] 
    return "CPU \\n 1m:%s 5m:%s 15m:%s" % (loadavg['lavg_1'], loadavg['lavg_5'], loadavg['lavg_15'])
