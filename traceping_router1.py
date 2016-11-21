from jnpr.junos import Device
from lxml import etree

dev1 = Device(host='192.168.34.16', user='user1', password='password1', port=22 )
dev.open()

cli=dev.rpc.ping(host="192.168.35.1")
print etree.tostring(cli)

cli=dev.rpc.traceroute(host="192.168.35.1")
print etree.tostring(cli)
