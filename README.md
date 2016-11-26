# sample_pyez
Sample code for using Juniper PyEZ


## sample code 1 : change hostname
How to run sample code 1

```
python set_firefly1_change_hostname.py
```

output

```                                                                                                                                                   (git)-[master]
% python set_firefly1_change_hostname.py                                                                                                                                                 (git)-[master]
##### Operation : Start #######
Connecting to device :  OK
Hostname :  firefly1
Load config :  OK
Target config : ./configs/change_hostname.conf
##############################
system {
    host-name firefly1_changed_by_PyEZ;
}
##############################
Diff :
##############################

[edit system]
-  host-name firefly1;
+  host-name firefly1_changed_by_PyEZ;

##############################
Commit Check :  OK
Do you commit? y/n
y
Commit candidate config : OK
Hostname :  firefly1_changed_by_PyEZ
##### Operation : End #####
```

## sample code 2 : add interface using Jinja2 Template

How to run sample code 1

```
python set_firefly1_add_interface.py 
```

```                                                                                                                                                      (git)-[master]
##### Operation : Start #######
Connecting to device :  OK
Hostname :  firefly1
Interfaces ge-0/0/2 :
##############################
<interface-information style="terse">
<physical-interface>
<name>
ge-0/0/2
</name>
<admin-status>
up
</admin-status>
<oper-status>
up
</oper-status>
</physical-interface>
</interface-information>

##############################
Load config :
OK
Target template : ./configs/add_interface.jinja2
##############################
interfaces {
   ge-0/0/2 {
        unit 0 {
            description add_by_PyEZ;
            family inet {
                address 192.168.35.1/30;
            }
        }
    }
}
##############################
Diff :
##############################

[edit interfaces]
+   ge-0/0/2 {
+       unit 0 {
+           description add_by_PyEZ;
+           family inet {
+               address 192.168.35.1/30;
+           }
+       }
+   }

##############################
Commit Check :  OK
Do you commit? y/n
y
Commit candidate config : OK
Interfaces ge-0/0/2 :
##############################
<interface-information style="terse">
<physical-interface>
<name>
ge-0/0/2
</name>
<admin-status>
up
</admin-status>
<oper-status>
up
</oper-status>
<logical-interface>
<name>
ge-0/0/2.0
</name>
<admin-status>
up
</admin-status>
<oper-status>
up
</oper-status>
<description>
add_by_PyEZ
</description>
<filter-information>
</filter-information>
<address-family>
<address-family-name>
inet
</address-family-name>
<interface-address>
<ifa-local emit="emit">
192.168.35.1/30
</ifa-local>
</interface-address>
</address-family>
</logical-interface>
</physical-interface>
</interface-information>

##############################
##### Operation : End #####

```