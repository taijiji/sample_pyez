#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyEZ
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

# color font
import colorama
from colorama import Fore

colorama.init(autoreset=True)

print "##### Operation : Start #######"

print "Connecting to device : ",
dev1 = Device(
            host="192.168.34.16",
            user="user1",
            password="password1"
        )   
dev1.open()
print Fore.GREEN + "OK"

print "Hostname : ",
print Fore.YELLOW + dev1.facts["hostname"]

dev1.bind(cu=Config)

print "Load config : ",
conf_filename = "./configs/change_hostname.conf"
dev1.cu.lock()
dev1.cu.load(
    path=conf_filename,
    format="text", # you can select text or set style
    merge=True
)
print Fore.GREEN + "OK" 

print "Target config : %s" % (conf_filename)
print "#"*30
with open(conf_filename, "r") as conf:
    print conf.read()
print "#"*30

print "Diff : "
print "#"*30
print dev1.cu.diff()
print "#"*30

print "Commit Check : ",
if dev1.cu.commit_check() :
    print Fore.GREEN + "OK"
else:
    print Fore.RED + "Error"

print Fore.YELLOW + "Do you commit? y/n"
choice = raw_input().lower()
if choice == "y":
    dev1.cu.commit()
    print "Commit candidate config : " + Fore.GREEN + "OK"
else:
    dev1.cu.rollback()
    print "Rollback : " + Fore.GREEN + "OK"

dev1.cu.unlock()
dev1.close()

dev1.open()
print "Hostname : ",
print Fore.YELLOW + dev1.facts["hostname"]
dev1.close()

print "##### Operation : End #####"
