基于x86架构的CentOS7虚拟机通过qemu安装ARM架构CentOS7虚拟机
----------------------------------------------------------

首先需要有一台CentOS虚拟机，如没有可参考
VMWare安装CentOS7操作系统的虚拟机 安装一台CentOS虚拟机
`参考连接 <https://blog.csdn.net/redrose2100/article/details/127862173>`__
### 安装基础命令

::

   yum install -y net-tools
   yum install -y wget

下载ARM架构的centos7操作系统镜像
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   mkdir -p /opt/os
   cd /opt/os
   wget http://mirror.nju.edu.cn/centos-altarch/7.9.2009/isos/aarch64/CentOS-7-aarch64-Minimal-2009.iso --no-check-certificate
   chmod 777 /opt/os/CentOS-7-aarch64-Minimal-2009.iso

下载ARM架构的EFI
~~~~~~~~~~~~~~~~

::

   yum install -y http://mirror.centos.org/altarch/7/os/aarch64/Packages/AAVMF-20180508-6.gitee3198e672e2.el7.noarch.rpm

安装基础依赖
~~~~~~~~~~~~

::

   yum groupinstall 'Development Tools' -y
   yum groupinstall "Virtualization Host" -y
   yum install -y kvm 
   yum install -y qemu 
   yum install -y virt-viewer 
   yum install -y virt-manager 
   yum install -y libvirt 
   yum install -y libvirt-python 
   yum install -y python-virtinst
   yum install -y libguestfs-tools 
   yum install -y virt-install.noarch 
   yum install -y virt-install 
   yum install -y virt-viewer 
   yum install -y virt-manager
   yum install -y python2 
   yum install -y zlib-devel 
   yum install -y glib2-devel 
   yum install -y pixman-devel 
   systemctl enable libvirtd
   systemctl start libvirtd
   usermod -aG libvirt $(whoami)

修改qemu配置文件
~~~~~~~~~~~~~~~~

::

   vim /etc/libvirt/qemu.conf

   放开
   user = "root"
   group = "root"

重启虚拟机
~~~~~~~~~~

::

   reboot

安装qemu
~~~~~~~~

::

   cd /opt
   wget https://download.qemu.org/qemu-4.2.0.tar.xz
   tar xf qemu-4.2.0.tar.xz
   cd qemu-4.2.0/
   ./configure --target-list=aarch64-softmmu --prefix=/usr
   make -j8
   make install

创建磁盘
~~~~~~~~

::

   rm -rf /home/dzl/qemu/images/test.img
   qemu-img create /home/dzl/qemu/images/test.img 30G

启动并安装虚拟机
~~~~~~~~~~~~~~~~

::

   安装ctenos8系统
   qemu-system-aarch64 -m 1024 -cpu cortex-a57 -smp 2 -M virt -bios /usr/share/AAVMF/AAVMF_CODE.fd -nographic -drive if=none,file=/home/dzl/qemu/os/CentOS-7-aarch64-Minimal-2009.iso,id=cdrom,media=cdrom -device virtio-scsi-device -device scsi-cd,drive=cdrom -drive if=none,file=/home/dzl/qemu/images/test.img,id=hd0 -device virtio-blk-device,drive=hd0

启动虚拟机
~~~~~~~~~~

::

   网络配置：
   配置宿主机网桥
   ifconfig
   ip tuntap add dev tap0 mode tap
   ip link set dev tap0 up
   ip address add dev tap0 192.168.2.128/24
   ifconfig

   route add -net 192.168.2.0 netmask 255.255.255.0 dev tap0
   iptables -t nat -A POSTROUTING -s 192.168.2.0/24 -o enp6s0 -j MASQUERADE

   启动虚拟机
   qemu-system-aarch64 -m 4096 -cpu cortex-a57 -smp 6 -M virt -bios /usr/share/AAVMF/AAVMF_CODE.fd -nographic -device virtio-scsi-device -drive if=none,file=/home/dzl/qemu/images/test.img,id=hd0 -device virtio-blk-device,drive=hd0  -net nic -net tap,ifname=tap0,script=no,downscript=no

   配置虚拟机ip
   ip addr add 192.168.2.129/24 dev eth0
   ip link set eth0 up

   ping宿主机查看联通情况
   ping 192.168.2.128

   虚机中添加default gw，即将虚机的网络数据包都交由物理机tap0处理
   route add default gw 192.168.2.128 dev eth0
