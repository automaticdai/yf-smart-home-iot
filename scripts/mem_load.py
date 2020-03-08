#!/usr/bin/python

from __future__ import print_function
from collections import OrderedDict

def mem_info():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

if __name__=='__main__':
    #print(meminfo())
    
    meminfo = mem_info()
    print('Total Memory: {0}'.format(meminfo['MemTotal']))
    print('Memory Free: {0}'.format(meminfo['MemAvailable']))
