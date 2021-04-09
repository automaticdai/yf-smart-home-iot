#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import weather
from collections import OrderedDict

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

def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo


if __name__=='__main__':    
	print "Content-type:text/html\r\n\r\n"
	print '<html>'
	print '<head>'
	print '<link rel="stylesheet" type="text/css" href="../pagestyle.css" />'
	print '<title>Xiaotian Dai HP Server</title>'
	print '</head>'
	print '<body>'

	# body starts from here
	print "<h1>HP Microserver Gen8 Status</h1>"
	print "<h2>Weather Report</h2>"
	weather.get_weather()

	print "<h2>CPU Info</h2>";
	lavg = load_stat()
	print "CPU Load (1 min): {0}</br>".format(lavg['lavg_1'])
	print "CPU Load (5 mins): {0}</br>".format(lavg['lavg_5'])
	print "CPU Load (15 mins): {0}</br>".format(lavg['lavg_15'])
    	
	meminfo = meminfo()
	print "<h2>Memory</h2>";
    	print 'Total memory: {0}</br>'.format(meminfo['MemTotal'])
    	print 'Free memory: {0}</br>'.format(meminfo['MemAvailable'])

	print "<h2>Environment</h2>";
	for param in os.environ.keys():
  		print "<b>%20s</b>: %s</br>"% (param, os.environ[param])
 	
	print '</body>'
	print '</html>'
