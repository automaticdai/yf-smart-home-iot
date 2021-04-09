#!/usr/bin/python

from __future__ import print_function
from collections import OrderedDict

def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return 'Total Mem {0} \\n Free Mem {1}'.format(meminfo['MemTotal'],meminfo['MemAvailable'])
