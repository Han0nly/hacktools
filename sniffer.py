#!usr/bin/env python
# coding=utf-8

import socket
import os

host = "192.168.0.196"

# 创建原始套接字,然后绑定在公开接口上
if os.name == "nt":
    socket_protocal = socket.IPPROTO_IP
else:
    socket_protocal = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocal)

sniffer.bind((host, 0))

# 设置在捕获的数据包中包含IP层
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

#
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print sniffer.recvfrom(65565)

# 在Windows平台上关闭混杂模式
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)
