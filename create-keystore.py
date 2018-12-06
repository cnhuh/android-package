#! /usr/bin/env python
# -*- coding:utf-8 -*-

#-- 使用Java密钥证书生成工具 keytool 生成 keystore --
#-- 由于使用的是Java工具，需要JRE进行环境支持，请确认已经安装JRE --
#-- 该代码中使用 python 调用os模块，通过cmd命令执行keytool程序 --

import os, time

print(os.path.abspath('.'))

str_alias = input("请输入keystore别名：")
#-- 创建文件生成目录 -- 在当前目录下，生成一个以别名命名的目录
filedir = os.path.join(os.path.abspath('.'), str_alias)
os.mkdir(filedir)

str_keystoredir = os.path.join(filedir,'key.keystore')
str_keypass = "simba.pro" #input("请输入keystore密码（默认与别名密码相同）：")

str_keytoolcmd = 'keytool -genkey -alias ' + str_alias \
    + ' -keypass ' + str_keypass \
    + ' -keyalg RSA  -validity 3650 -keystore ' + str_keystoredir \
    + ' -storepass ' + str_keypass \
    + ' -dname "CN=(cnhuh), OU=(aot), O=(aot), L=(fz), ST=(fj), C=(cn)"'
os.popen(str_keytoolcmd)


#-- 检查keystore 是否已经生成
while os.path.exists(str_keystoredir) == False:
    time.sleep(0.5)

str_keystorelogfile = os.path.join(filedir,'output.log')
f = open(str_keystorelogfile, 'w')
str_outputlogcmd = 'keytool -v -list -keystore ' + str_keystoredir + ' -storepass ' + str_keypass
f.write(os.popen(str_outputlogcmd).read())

f = open(str_keystorelogfile, 'a')
str_outputlogcmd = 'keytool -list -rfc -keystore ' + str_keystoredir + ' -storepass ' + str_keypass
f.write(os.popen(str_outputlogcmd).read())

