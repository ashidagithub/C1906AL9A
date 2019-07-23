# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习使用 csv 文件写一副牌
#   学习使用 加密技术 文件写一副牌
# ------------------------(max to 80 columns)-----------------------------------
import rsa

from machine.std_mach import create_deck_54, record_deck_csv, read_deck_csv

# phase 1:   不加密
csv_name = '不加密的54张扑克牌.csv'
deck=[]
deck1=[]
create_deck_54(deck1)
deck.extend(deck1)
deck2=[]
create_deck_54(deck2)
deck.extend(deck1)
record_deck_csv(deck, csv_name)

deck = []
read_deck_csv(csv_name, deck)
print('--debug: 54 deck: \n%s' % (deck))

# Phase 2： 加密
msg = ",".join(deck)
print('--debug: 54 deck to string: %s\n' % msg)

# 生成一对密钥
key = rsa.newkeys(4500)
public_key = key[0]
private_key = key[1]
#print('--debug: my public key is [%s], \nmy private key is [%s] ' %
#      (public_key, private_key))

# 用公钥加密
byte_msg = msg.encode()
crypted_msg = rsa.encrypt(byte_msg, public_key)
print('--debug: crypted deck is %s' % crypted_msg)

# 用私钥解密
byte_msg = rsa.decrypt(crypted_msg, private_key)
msg = byte_msg.decode()
print('--debug: restored deck is %s' % msg)
