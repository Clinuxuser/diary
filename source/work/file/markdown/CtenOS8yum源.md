## CtenOS8yum源

```
1、 备份原来的yum 源
    mkdir  /tmp/yum
    cd /etc/yum.repos.d
    mv *.repo /tmp/yum
    
2.配置域名

    vi /etc/sysconfig/network-scripts/ifcfg-enp0s3
    DNS1=8.8.8.8 //加上
    DNS2=114.114.114.114 //加上
    ZONE=public //加上

2、 下载阿里的yum 源

    wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo
    
3、 清除yum缓存再重新生成yum缓存
    yum clean all
    yum makecache
```


```
mkdir  /tmp/yum
cd /etc/yum.repos.d
mv *.repo /tmp/yum
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo
yum clean all
yum makecache
```