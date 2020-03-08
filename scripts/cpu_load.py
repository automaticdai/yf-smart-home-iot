#!/usr/bin/python  
 
import os 

def cpu_stat(): 
    loadavg = {} 
    with open("/proc/loadavg") as f:
    	con = f.read().split()
    	loadavg['1'] = con[0] 
   	loadavg['5'] = con[1] 
    	loadavg['15'] = con[2] 
    	loadavg['nr'] = con[3] 
    	loadavg['last_pid'] = con[4] 
    return loadavg 

if __name__ == "__main__":
	lavg = cpu_stat()
	print "loadavg %s %s %s" % (lavg['1'], lavg['5'], lavg['15'])
