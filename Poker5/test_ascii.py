# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习 ASCII 码
# ------------------------(max to 80 columns)-----------------------------------
import random

print('A')
print(chr(65),chr(65))

for k in range(33,127):
    print ('ASC CODE (%d) is %c' % (k, chr(k)))

password = []
for k in range(16):
    asc_code = random.randint(33,128)
    password.extend(chr(asc_code))
print('-- password is --->', password )
