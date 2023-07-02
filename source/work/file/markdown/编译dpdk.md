# dpdk

## 编译

### 安装依赖

    yum install -y gcc 
    um install -y python3
    yum install -y python-pyelftools
    pip3 install pyelftools
    pip3 install meson
    pip3 install ninja
    export PKG_CONFIG_PATH=/usr/local/lib64/pkgconfig/

### 编译安装dpdk

    meson build
    cd build
    ninja install -j8

### 添加igb_uio模块

#### igb_uio下载

原文[参考路径]  
igb_uio[下载路径]

##### 方式一:直接添加到文件中
>
> 解压上面下载的 dpdk-kmods-main.tar.gz  
    添加修改 对应的模块，设置对应参数

1. 复制 dpdk-kmods/linux/igb_uio/ 到 dpdk-stable-21.11.1/kernel/linux/ 目录下  

```
    cp dpdk-kmods-main/linux/igb_uio/ ../dpdk-stable-21.11.1/kernel/linux/ -r
```

2. 修改 meson.build 代码

```
vi dpdk-stable-21.11.1/kernel/linux/meson.build +4
---
subdirs = ['kni', 'igb_uio']            #修改： 添加 igb_uio
```

3. 创建 igb_uio 模块的编译代码

```
创建文件 meson.build 在 dpdk*/kernel/linux/igb_uio/ 目录下
添加如下代码到 新创建的 meson.build 文件中
# ----start----
# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2017 Intel Corporation
 
mkfile = custom_target('igb_uio_makefile',
  output: 'Makefile',
  command: ['touch', '@OUTPUT@'])
 
custom_target('igb_uio',
  input: ['igb_uio.c', 'Kbuild'],
  output: 'igb_uio.ko',
  command: ['make', '-C', kernel_dir + '/build',
    'M=' + meson.current_build_dir(),
    'src=' + meson.current_source_dir(),
    'EXTRA_CFLAGS=-I' + meson.current_source_dir() +
    '/../../../lib/librte_eal/include',
    'modules'],
  depends: mkfile,
  install: true,
  install_dir: kernel_dir + '/extra/dpdk',
  build_by_default: get_option('enable_kmods'))       
# ----end----
```

4. 添加IGB_UIO的编译使能

```
修改 dpdk-stable-21.11.1/meson_options.txt  文件
---
enable_kmods   value值 变成 true
```

5. 添加 kernel_dir 的定义

```
在 dpdk-stable-21.11.1/meson.build  添加 kernel_dir 的定义
---
    kernel_version = run_command('uname', '-r').stdout().strip()
    kernel_dir = '/lib/modules/' + kernel_version
```

6. 执行编译

##### 二、 外部直接编译  

进入目录，直接make  
> igb_uio 目录下的 MakeFile 可以直接用，啥都不用干

    cd dpdk-kmods-main/linux/igb_uio/
    make

[下载路径]:https://git.dpdk.org/dpdk-kmods/commit/?id=e68a705cc5dc3d1333bbcd722fe4e9a6ba3ee648
[参考路径]:https://www.cnblogs.com/qz652219228/archive/2022/09/24/16712813.html
