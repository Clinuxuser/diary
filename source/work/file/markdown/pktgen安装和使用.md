## pktgen

### 参加路径
<https://pktgen-dpdk.readthedocs.io/en/latest/commands.html#runtime-options-and-commands>
<https://blog.csdn.net/kelxLZ/article/details/114289332>
pktgen常用命令:
```
start 0 // 启动网口 0 的发包过程
stop 0 // 停止网口 0 的发包过程
str  // 开启所有网卡法宝过程 等于start all 
stp // 停止所有网口的发包过程 等于stop all 


range all proto udp 
//设置udp协议

set all size 64 
//设置数据包大小为64字节

set all rate 100 
//设置发送速率

enable all range  
//启用range功能

enable all random 
//启用随机包功能

set 0 count 1
//只发一个包
```
set all proto udp
set all size 64
set all rate 100
range all dst ip start 0.0.0.0
range all dst ip min 0.0.0.0
range all dst ip max 1.2.3.4
range all dst ip inc 0.0.1.0
range all src ip start 0.0.0.0
range all src ip min 1.1.1.1
range all src ip max 2.2.2.2
range all src ip inc 1.1.2.1


enable all range  

str 


```


```
27a2c6ff3885227ce4d5be9360d1f8299feb3605
7867b0d9b0b11ca84057b73a2ad8a3694a56e0ed


enable/disable
```
process：启用或禁用ARP / ICMP / IPv4 / IPv6数据包处理

mpls：启用/禁用在数据包中发送MPLS条目

qinq：启用/禁用在数据包中发送Q-in-Q标头

gre：启用/禁用GRE支持

gre_eth：启用/禁用以太网帧负载GRE支持

vlan：启用/禁用VLAN标记

garp：启用或禁用免费ARP数据包处理

random：启用/禁用随机数据包支持

latency：启用/禁用延迟测试

pcap：启用或禁用在端口列表上发送pcap数据包

blink：启用或禁用端口上的LED闪烁

rx_tap：启用/禁用RX Tap支持

tx_tap：启用/禁用TX Tap支持

icmp：启用/禁用发送ICMP数据包

range：启用或禁用给定的端口列表以发送一定范围的数据包

capture：在端口列表上启用/禁用数据包捕获

bonding：在绑定设备中启用或禁用发送0内容数据包

short：允许发送短于64字节的帧

vxlan：启用或禁用发送VxLAN数据包

screen：启用/禁用更新屏幕和解锁/锁定窗口

mac_from_arp：启用/禁用ARP数据包中的MAC地址

off：屏幕关闭快捷方式

on：屏幕开启快捷方式
```

set 
```
set <portlist> count <value>：发送报文数量

set <portlist> size <value>：发送报文大小

set <portlist> rate <percent>：发送报文速率百分比

set <portlist> burst <value>：批量收发报文数量

set <portlist> tx_cycles <value>：调试以设置每个TX突发的周期数

set <portlist> sport <value>：TCP源端口号

set <portlist> dport <value>：TCP目的端口号

set <portlist> seq_cnt|seqcnt|seqCnt <value>：设置发送顺序中的包数[0-16]

set <portlist> prime <value>：设置在prime命令上发送的数据包数量

set <portlist> dump <value>：将接下来的N个接收到的数据包转储到屏幕上

set <portlist> vlan <value>：设置端口列表的VLAN ID值

set <portlist> jitter <value>：设置抖动阈值（以微秒为单位）

set <portlist> src|dst mac <addr>：设置源端口或者目的端口MAC地址00：11：22：33：44：55或0011：2233：4455格式

set <portlist> type ipv4|ipv6|vlan|arp：将数据包类型设置为IPv4或IPv6或VLAN

set <portlist> proto udp|tcp|icmp：将每个端口的数据包协议设置为UDP或TCP或ICMP

set <portlist> pattern <type>：设置填充数据类型

abc：默认填充的数据为字符串abc
none：没有填充模式，可能是随机数据
zero：不填充任何数据
user：用户提供的最大16个字节的字符串
set <portlist> user pattern <string>：一个16字节的字符串，必须在之前设置pattern user命令

set <portlist> [src|dst] ip ipaddr：设置源IP地址或者目的IP地址，格式类似10.1.2.3/24

set <portlist> qinqids <id1> <id2>：设置端口列表的Q-in-Q ID

set <portlist> rnd <idx> <off> <mask>：为端口列表中的所有传输数据包设置随机掩码

idx：随机掩码索引槽
off：以字节为单位的偏移量，以应用掩码值
mask：最长32位长的掩码规范（可禁用）：
0：位将为0
1：位将为1
.：位将被忽略（保留原始值）
X：位将获得随机值
set <portlist> cos <value>：设置端口列表的cos值

set <portlist> tos <value>：设置端口列表的tos值

set <portlist> vxlan <flags> <group id> <vxlan_id>：设置vxlan值

set ports_per_page <value>：设置每页端口值1-6

```

range命令主要用于设置包内容的随机数值范围，例如
```
对于每一个参数选项，我们都需要设置SMMI，也就是这个参数的起始值、最小值、最大值和增量

range <portlist> src|dst mac <SMMI> <etheraddr>：设置目的或者源MAC地址
一些例子
range 0 src mac start 00:00:00:00:00:00
range 0 dst mac max 00:12:34:56:78:90
range 0 src mac 00:00:00:00:00:00 00:00:00:00:00:00 00:12:34:56:78:90 00:00:00:01:01:01
range <portlist> src|dst ip <SMMI> <ipaddr>：设置目的或者源IP地址
一些例子
range 0 dst ip start 0.0.0.0
range 0 dst ip min 0.0.0.0
range 0 dst ip max 1.2.3.4
range 0 dst ip inc 0.0.1.0
range 0 dst ip 0.0.0.0 0.0.0.0 1.2.3.4 0.0.1.0
range <portlist> proto tcp|udp：设置IP协议类型
range <portlist> src|dst port <SMMI> <value>：设置UDP和TCP的源或目的端口
或者另一种形式range <portlist> src|dst port <start> <min> <max> <inc>
range <portlist> vlan <SMMI> <value>：设置VLAN ID的起始地址
range <portlist> vlan <start> <min> <max> <inc>
range <portlist> size <SMMI> <value>：设置包的大小
range <portlist> size <start> <min> <max> <inc>
range <portlist> teid <SMMI> <value>：设置TEID值
range <portlist> mpls entry <hex-value>：设置MPLS表项值
range <portlist> qinq index <val1> <val2>：设置qinq
range <portlist> gre key <value>：设置gre
range <portlist> cos <SMMI> <value>：设置cos
range <portlist> tos <SMMI> <value>：设置tos

```