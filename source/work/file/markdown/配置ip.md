### 配置ip: 
ip address add 192.168.10.28/24 dev enp7s0

### 配置网关
route add default gw 192.168.10.1

### 配置路由：
ip route add 192.168.10.0/24 via 192.168.10.28

添加一条路由(发往192.168.62这个网段的全部要经过网关192.168.1.1)
route add -net 192.168.62.0 netmask 255.255.255.0 gw 192.168.1.1

麒麟系统配置ip
修改配置文件:
vim /etc/network/interfaces
```
auto enaphyt4i0
iface enaphyt4i0 inet static
address 192.168.123.29
netmask 255.255.255.0
gateway 192.168.123.1
```
service networking restart


