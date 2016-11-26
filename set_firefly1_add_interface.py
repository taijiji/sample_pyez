#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyEZ
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

# color font
import colorama
from colorama import Fore

# for print for interface-information 
from lxml import etree

# Jinja2 Template Engine
from jinja2 import Template, Environment

colorama.init(autoreset=True)

print "##### Operation : Start #######"

print "Connecting to device : ",
dev1 = Device(
            host="192.168.34.16",
            user="user1",
            port=22, # NETCONF port (defaults to 830)
            password="password1"
        )   
dev1.open()
print Fore.GREEN + "OK"

print "Hostname : ",
print dev1.facts["hostname"]

print "Interfaces ge-0/0/2 : "
print "#"*30
if_info = dev1.rpc.get_interface_information(
                    interface_name='ge-0/0/2',
                    terse=True
                    )
print Fore.YELLOW + etree.tostring(if_info)
print "#"*30

dev1.bind(cu=Config)

print "Load config : "
template_filename = "./configs/add_interface.jinja2"
add_if_param = {
    'if_name' : 'ge-0/0/2',
    'if_description' : 'add_by_PyEZ',
    'if_address_ipv4' : '192.168.35.1',
    'if_subnet_ipv4' : '30'
}
dev1.cu.lock()
dev1.cu.load(
    template_path=template_filename, 
    template_vars=add_if_param, 
    format="text",
    merge=True
)
print(Fore.GREEN + 'OK')

print "Target template : %s" % (template_filename)
print "#"*30
with open(template_filename, 'r') as conf:
    template_txt = conf.read()
    print Environment().from_string(template_txt).render(add_if_param)
print "#"*30

print "Diff : "
print "#"*30
print dev1.cu.diff()
print "#"*30

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

dev1.open()
print "Interfaces ge-0/0/2 : "
print "#"*30
if_info = dev1.rpc.get_interface_information(
                    interface_name='ge-0/0/2',
                    terse=True
                    )
print Fore.YELLOW + etree.tostring(if_info)
print "#"*30
dev1.close()

print "##### Operation : End #####"
