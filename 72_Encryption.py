#Day 72: Encryption Basics
#
#

import hashlib



encryption1 = hashlib.sha256(b'12 widgets for 1 superwidget')
str_hex1 = encryption1.hexdigest()
encryption2 = hashlib.sha256(b'6 widgets for 1 sprocket')
str_hex2 = encryption2.hexdigest()
encryption3 = hashlib.sha256(b'2 sprockets for 1 superwidget')
str_hex3 = encryption3.hexdigest()
encryption4 = hashlib.sha256(b'24 widgets for 1 superwidget and 2 sprockets')
str_hex4 = encryption4.hexdigest()

block = [str_hex1, str_hex2, str_hex3, str_hex4]

print(block)
