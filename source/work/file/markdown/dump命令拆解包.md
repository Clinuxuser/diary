
1、tcpdump 将pcap数据包按照文件大小100M拆解保存。
```
    1. 将pcap数据包文件拷贝到 /var/tmp目录下   
    2. 在/tmp目录下   tcpdump -r 数据包文件名称  -C 100M -w  test
```

2、tcpdump 将pcap数据包按照协议拆解保存。
```

1. 只保存bgp协议数据包
tcpdump -r 数据包文件名称  port 179   -w test

1. 只保存OSPF协议数据包
tcpdump -r 数据包文件名称  ip proto ospf  -w test

1. 只保存ISIS协议数据包
tcpdump -r 数据包文件名称  isis  -w test
```