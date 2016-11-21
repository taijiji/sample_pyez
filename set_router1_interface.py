#! /usr/bin/env python
# -*- coding: utf-8 -*-
import yaml

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

dev1 = Device(host='192.168.34.16', user='user1', password='password1', port=22 )

dev1.open()
dev1.bind(cu=Config)

print "Host name : %s" % ( dev1.facts['hostname'] )
print "Model : %s" % ( dev1.facts['model'] )
print "version: %s" % ( dev1.facts['version'] )


print "Load config : ",

dev1.cu.lock()
#conf_filename = "./configs/change_hostname.conf"
#dev1.cu.load(path=conf_filename, format="text", merge=True)
template_filename = "./configs/set_interface.conf"
param_dict = yaml.load(open("./configs/param_interface.yml"))
dev1.cu.load(
    template_path=template_filename, 
    template_vars=param_dict, 
    format="text",
    merge=True)


print(Fore.GREEN + 'OK')

#print "Target config : %s" % (conf_filename)
#with open(conf_filename, 'r') as conf:
#    print conf.read()

print "Diff : "
print dev1.cu.diff()

print "Commit Check : ",
if dev1.cu.commit_check() :
    print(Fore.GREEN + 'OK')
else:
    print(Fore.RED + 'Error')

print "Do you commit? y/n"
choice = raw_input().lower()
if choice == 'y':
    dev1.cu.commit()
    print "Commit candidate config : " + Fore.GREEN + "OK"
else:
    dev1.cu.rollback()
    print "Rollback : " + Fore.GREEN + "OK"

dev1.cu.unlock()
dev1.close()

"Operation : Finished"
