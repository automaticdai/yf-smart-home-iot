#!/usr/bin/python
# -*- coding: utf-8 -*-
#by ljk 20160526
 
import os,re,sys,time
 
if len(sys.argv) == 1:
    print('\n')
    sys.exit(100)
else:
    print('start monitoring,press "ctrl+c" to stop\n')
 
    for arg in sys.argv[1:]:    #输出标头
        header = '------{} bandwidth(Mb/s)------'.format(arg)
    print()
 
    #global values_dic
    values_dic = {}    #定义空字典，用来在下面函数中存放各网卡的各项需要用到的值
 
    def get_values(orders):
        try:
            with open('/proc/net/dev') as f:
                lines=f.readlines()    #内容不多，一次性读取较方便
                for arg in sys.argv[1:]:
                    for line in lines:
                        line=line.lstrip()    #去掉行首的空格，以便下面split
                        if re.match(arg,line):
                            values = re.split("[ :]+",line)    #以空格和:作为分隔符
                            values_dic[arg+'r'+orders]=values[1]    #1为接收值
                            values_dic[arg+'t'+orders]=values[9]    #9为发送值
                            #return [values[1],values[9]]    #可返回列表
        except (FileExistsError,FileNotFoundError,PermissionError):
            print('open file error')
            sys.exit(-1)
 
    try:
        while True:
            get_values('first')    #第一次取值
            time.sleep(10)
            get_values('second')    #10s后第二次取值
 
            for arg in sys.argv[1:]:
                r_bandwidth = (int(values_dic[arg+'r'+'second']) - int(values_dic[arg+'r'+'first']))/1024.0/1024/10*8
                t_bandwidth = (int(values_dic[arg+'t'+'second']) - int(values_dic[arg+'t'+'first']))/1024.0/1024/10*8
                print('IN: '+str(round(r_bandwidth,2)).ljust(8)+'  OUT: '+str(round(t_bandwidth,2)))
 
            print()
            values_dic = {}    #清空本次循环后字典的内容
    except KeyboardInterrupt:
        print("\n-----bye-----")



