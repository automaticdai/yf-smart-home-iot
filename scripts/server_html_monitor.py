#!/usr/bin/python

import time
import os

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

if __name__ == '__main__':
	diff =  os.system("diff -ru /www/html/homepage /www/html/.homepage")

	if (diff != 0):
		with cd('/www/html/homepage/'):
			os.system("make clean")
			os.system("make")
		os.system("rm -rf /www/html/.homepage/")
		os.system("cp -rf /www/html/homepage/ /www/html/.homepage/")
	
