# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习使用 csv 文件写一副牌
#   学习使用 加密技术 文件写一副牌
# ------------------------(max to 80 columns)-----------------------------------
import rsa

from machine.std_mach import *

# phase 1:   不加密
csv_name = '不加密的54张扑克牌.csv'
deck = []
create_deck_54(deck)
record_deck_csv(deck, csv_name)

deck = []
read_deck_csv(csv_name, deck)
print('--debug: 54 deck: \n%s' % (deck))

# Phase 2： 加密
msg = ",".join(deck)
print('--debug: 54 deck to string: %s\n' % msg)

# 生成一对密钥
key = rsa.newkeys(3072)
public_key = key[0]
private_key = key[1]
print('--debug: my public key is [%s], \nmy private key is [%s] ' %
      (public_key, private_key))

# 用公钥加密
#msg = 'test for crypte '
crypted_msg = rsa.encrypt(msg.encode(), public_key)
print('--debug: crypted message is %s' % crypted_msg)

# 用私钥解密
msg = rsa.decrypt(crypted_msg, private_key)
print('--debug: original message is %s' % msg.decode())
