windows下安装qemu
-----------------

`原文路径 <https://blog.csdn.net/EmptyStupid/article/details/127949231>`__
`引导文件 <https://releases.linaro.org/components/kernel/uefi-linaro/16.02//release/qemu64/>`__
`虚拟网卡安装包 <http://swupdate.openvpn.net/community/releases/tap-windows-9.21.2.exe>`__
`虚拟网卡配置参考 <https://zhuanlan.zhihu.com/p/679214589>`__
`参考:1 <https://www.cnblogs.com/mylibs/p/kylin-arm64-with-qemu-on-windows.html>`__

目录结构
~~~~~~~~

::

  qemu目录：
  D::raw-latex:`\azdd`:raw-latex:`\qemu`:raw-latex:`\qemu`-install:raw-latex:`\qemu`
  虚拟机目录
  D::raw-latex:`\azdd`:raw-latex:`\qemu`:raw-latex:`\project`:raw-latex:`\kylin`
  ios镜像目录
  D::raw-latex:`\azdd`:raw-latex:`\qemu`:raw-latex:`\qemu`-install

创建tap0网卡
~~~~~~~~~~~~

下载\ `虚拟网卡安装包 <http://swupdate.openvpn.net/community/releases/tap-windows-9.21.2.exe>`__
进行安装，并将安装后的tap-windows网卡名称修改为tap0
并将以太网设置成共享internet连接

创建qemu虚拟磁盘
~~~~~~~~~~~~~~~~

进入虚拟机目录：

::

   cd  D:\azdd\qemu\project\kylin
   qemu-img.exe create -f qcow2 kylindisk.qcow2 120G 

安装kylin系统
~~~~~~~~~~~~~

将之前下载的EFI文件拷贝到创建的镜像目录中（不拷贝也可以，使用-bios选项指定即可，拷贝是为了方便以后找到该文件，防止不小心删除了该文件）。
在cmd界面中，使用qemu-system-aarch64.exe命令安装麒麟操作系统： >
注意：此处安装的是麒麟V10SP3

::

   qemu-system-aarch64.exe -m 8192 -cpu cortex-a72 -smp 8,sockets=4,cores=2 -M virt -bios D:\azdd\qemu\project\kylin\QEMU_EFI.fd -device VGA -device nec-usb-xhci -device usb-mouse -device usb-kbd -drive if=none,file=D:\azdd\qemu\project\kylin\kylindisk.qcow2,id=hd0 -device virtio-blk-device,drive=hd0 -drive if=none,file=D:\azdd\qemu\qemu-install\Kylin-Server-10-SP2-Release-Build09-20210524-arm64.iso,id=cdrom,media=cdrom -device virtio-scsi-device -device scsi-cd,drive=cdrom -net nic -net tap,ifname=tap0

启动
~~~~

::

   qemu-system-aarch64.exe -m 8192 -cpu cortex-a72 -smp 8,sockets=4,cores=2 -M virt -bios D:\azdd\qemu\project\kylin\QEMU_EFI.fd -device VGA -device nec-usb-xhci -device usb-mouse -device usb-kbd -drive if=none,file=D:\azdd\qemu\project\kylin\kylindisk.qcow2,id=hd0 -device virtio-blk-device,drive=hd0 -device virtio-scsi-device -net nic -net tap,ifname=tap0

ip:192.168.137.99 密码：wangtai@0720
