# sample_pyez
Sample code for using Juniper PyEZ


## sample code 1 : change hostname
How to run sample code 1

```
python set_firefly1_change_hostname.py
```

output

```                                                                                                                                                   (git)-[master]
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
```