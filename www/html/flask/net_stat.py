#!/usr/bin/python
import time
import sys

INTERFACE = 'eno2'
STATS = []

def	rx():
	ifstat = open('/proc/net/dev').readlines()
	for interface in ifstat:
		if 'eno2' in interface:
			stat = float(interface.split()[1])
			STATS[0:] = [stat]

def	tx():
	ifstat = open('/proc/net/dev').readlines()
	for interface in  ifstat:
		if 'eno2' in interface:
			stat = float(interface.split()[9])
			STATS[1:] = [stat]

def	netstat():
	rx()
	tx()
	time.sleep(1)
	rxstat_o = list(STATS)
	rx()
	tx()
	RX = float(STATS[0])
	RX_O = rxstat_o[0]
	TX = float(STATS[1])
	TX_O = rxstat_o[1]
	RX_RATE = round((RX - RX_O)/1024/1024,3) 
	TX_RATE = round((TX - TX_O)/1024/1024,3)
	return 'Tx:{:.3f} MB Rx:{:.3f} MB'.format(RX_RATE, TX_RATE)

