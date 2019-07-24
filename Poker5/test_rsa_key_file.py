# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习使用 rsa 加密技术创建和使用 公钥文件及密钥文件
# ------------------------(max to 80 columns)-----------------------------------
import rsa

# 先生成一对密钥，然后保存.pem格式文件，当然也可以直接使用
key = rsa.newkeys(1024)
public_key = key[0]
private_key = key[1]

# 将公钥及私钥写入key文件
pub = public_key.save_pkcs1()
pubfile = open('public.pem', 'wb')
pubfile.write(pub)
pubfile.close()

pri = private_key.save_pkcs1()
prifile = open('private.pem', 'wb')
prifile.write(pri)
prifile.close()




# 读取公钥进行加密
with open('public.pem') as publickfile:
    p = publickfile.read()
    public_key = rsa.PublicKey.load_pkcs1(p)

# 用公钥加密
msg = 'message for testing......'
byte_msg = msg.encode()
crypted_msg = rsa.encrypt(byte_msg, public_key)
print('--debug: crypted message is [%s]' % crypted_msg)

# 读取私钥进行解密解密
with open('private.pem') as privatefile:
    p = privatefile.read()
    private_key = rsa.PrivateKey.load_pkcs1(p)

byte_msg = rsa.decrypt(crypted_msg, private_key)
msg = byte_msg.decode()
print('--debug: original message is [%s]' % msg)
