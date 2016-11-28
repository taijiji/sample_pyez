#! /usr/bin/env python
# -*- coding: utf-8 -*-

# PyEZ
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

# Jinja2 Template Engine
from jinja2 import Template, Environment

# color font
import colorama
from colorama import Fore

# Init color font
colorama.init(autoreset=True)


print "##### Operation : Start #######"

print "Connecting to device : ",
dev1 = Device(
            host        = "192.168.34.16",
            user        = "user1",
            password    = "password1"
        )   
dev1.open()
print Fore.GREEN + "OK"

print "Hostname : ",
print Fore.YELLOW + dev1.facts["hostname"]

dev1.bind(cu=Config)

print "Load config : ",
template_filename = "./configs/add_policy.jinja2"
param_add_policy = {
    "policy_name"               : "AS65002_export_policy_add_by_PyEZ",
    "advertised_address_ipv4"   : "10.10.10.0",
    "advertised_subnet_ipv4"    : "24",
    "interface_name"            : "ge-0/0/2",
    "neighbor_address_ipv4"    : "192.168.35.2"
}
dev1.cu.lock()
dev1.cu.load(
    template_path   = template_filename, 
    template_vars   = param_add_policy, 
    format          = "text",
    merge           = True
)
print Fore.GREEN + "OK" 

print "Target config : "
print "#"*30
with open(template_filename, 'r') as conf:
    template_txt = conf.read()
    print Environment().from_string(template_txt).render(param_add_policy)

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

print "##### Operation : End #####"
