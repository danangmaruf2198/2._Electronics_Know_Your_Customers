from Tkinter import *
import atexit
import os

try:
    _count = int(open("counter").read())
except IOError:
    _count = 0

def incrcounter(n):
    global _count
    _count = _count + n

def savecounter():
    print 'asd'
    os.chdir('/media/pi/ANONYMOUS1/mechlab/ekyc')
    open("counter.txt", "w+").write("just try %d\r\n" % (555))

def keluar():
    exit()
