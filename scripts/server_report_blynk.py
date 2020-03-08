#!/usr/bin/python
import urllib2
from cpu_load import cpu_stat
from mem_load import mem_info
import os, re, sys, time


auth_token = "3824f24ccc814ed6a328261548cd6baa"


def report(vpin, value):
	try:
		urllib2.urlopen('http://blynk-cloud.com/' + auth_token + '/update/' + vpin + '?value=' + value)	
	except:
		print('Network failure ...')
	return


values_dict = {}

def get_net_stat(orders):
	with open('/proc/net/dev') as f:
		lines=f.readlines() 
		arg = "eno2"
		for line in lines:
			line=line.lstrip() 
			if re.match(arg,line):
				values = re.split("[ :]+",line)   
				values_dict[arg+'r'+orders]=values[1] 
				values_dict[arg+'t'+orders]=values[9]  
				#return [values[1],values[9]]    


cnt = 0

while True:
	print('logging...%d' % cnt)
	cnt = cnt + 1

	# cpu
	load = cpu_stat()

	report('V0', load['1'])
	report('V1', load['5'])
	report('V2', load['15'])

	# memory
	meminfo = mem_info()
	#print('Total Memory: {0}'.format(meminfo['MemTotal']))
	#print('Memory Free: {0}'.format(meminfo['MemAvailable']))

	report('V3', meminfo['MemTotal'].replace (" ", "+"))
	report('V4', meminfo['MemAvailable'].replace (" ", "+"))
	

	# network
	get_net_stat('first')
	time.sleep(10)

	get_net_stat('second')

	arg = "eno2"

	r_bandwidth = (int(values_dict[arg+'r'+'second']) - int(values_dict[arg+'r'+'first']))/1024.0/10
	t_bandwidth = (int(values_dict[arg+'t'+'second']) - int(values_dict[arg+'t'+'first']))/1024.0/10
	print('IN: '+str(round(r_bandwidth,2)).ljust(8)+'  OUT: '+str(round(t_bandwidth,2)).ljust(16))

	report('V5', '%.1f' % r_bandwidth)
	report('V6', '%.1f' % t_bandwidth)
	
	values_dict = {}

