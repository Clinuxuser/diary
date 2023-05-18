证书管理流程
------------

环境：安装openssl1.1.1
~~~~~~~~~~~~~~~~~~~~~~

一、生成根证书
^^^^^^^^^^^^^^

1、生成根证书私钥 – pem文件
'''''''''''''''''''''''''''

::

    openssl genrsa -out cakey.pem 2048

2、生成根证书签发申请文件 – csr文件（此步需要填写CN、BJ等信息）
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

::

    openssl req -new -key cakey.pem -out ca.csr

3、自签发根证书 – crt文件
'''''''''''''''''''''''''

::

   openssl x509 -req -days 36500 -sha1 -extensions v3_ca -signkey cakey.pem -in ca.csr -out root.crt

4.查看证书有效期
''''''''''''''''

::

   openssl x509 -in root.crt -noout -dates

二、用根证书签发服务端证书
^^^^^^^^^^^^^^^^^^^^^^^^^^

1、生成服务端私钥
'''''''''''''''''

::

   openssl genrsa -out server.key 2048

2、生成根证书请求文件
'''''''''''''''''''''

::

   openssl req -new -key server.key -out server.csr

3、使用根证书签发服务端证书
'''''''''''''''''''''''''''

::

   openssl x509 -req -days 36500 -sha1 -extensions v3_req -CA root.crt -CAkey cakey.pem -CAserial ca.srl -CAcreateserial -in server.csr -out server.crt

4、转换pkcs8版本
''''''''''''''''

::

   openssl pkcs8 -topk8 -inform PEM -in server.key -outform PEM -nocrypt -out pkcs8_server.pem

三、用根证书签发客户端证书
^^^^^^^^^^^^^^^^^^^^^^^^^^

1、生成客户端私钥
'''''''''''''''''

::

   openssl genrsa -out client.key 2048

2、 生成证书请求文件
''''''''''''''''''''

::

   openssl req -new -key client.key -out client.csr

3、使用根证书签发客户端证书
'''''''''''''''''''''''''''

::

   openssl x509 -req -days 36500 -sha1 -extensions v3_req -CA root.crt -CAkey cakey.pem -CAserial ca.srl -in client.csr -out client.crt

.. _转换pkcs8版本-1:

4、转换pkcs8版本
'''''''''''''''''''''

::

   openssl pkcs8 -topk8 -inform PEM -in client.key -outform PEM -nocrypt -out pkcs8_client.pem

四、用根证书签发规则加解密公私钥对
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.OpenSSL生成私钥
'''''''''''''''''

::

   openssl genrsa -out rsa_private_key.pem 2048  

2.OpenSSL生成公钥
'''''''''''''''''

::

   openssl rsa -in rsa_private_key.pem -pubout -out rsa_public_key.pem  

3.RSA私钥转换成PKCS8格式
''''''''''''''''''''''''

::

   openssl pkcs8 -topk8 -inform PEM -in rsa_private_key.pem -outform PEM -nocrypt

五、JAVA存储位置
^^^^^^^^^^^^^^^^

1.通道证书
''''''''''

::

   /usr/local/.config/ssl/
   root.crt 根证书
   client.crt  pkcs8_client.key  pkcs8_server.key    server.crt

2. 加解密公私钥
'''''''''''''''

六、RFW存储位置
^^^^^^^^^^^^^^^

.. _通道证书-1:

1.通道证书
''''''''''''''

::

   /opt/rfw/cert
   root.crt 根证书
   client.crt 客户端证书 原client.pem  
   client.key 客户端私钥 原private.pem  

.. _加解密公私钥-1:

2.加解密公私钥
''''''''''''''''''

::

   app/source/rfw/alg-security/pem_key.c:char rsa_public_key[1024]
