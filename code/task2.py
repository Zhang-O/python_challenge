#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

#  string 已经没有maketrans方法了  maketrans成了str的静态方法  版本变得太快
# from string import maketrans

my_str = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb\
 rfyr q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
alphabet_dict = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",
				 16:"p",17:"q", 18: "r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
alphabet_dict2 = {"y":"a","z":"b",'a':"c",'b':"d",'c':"e",'d':"f","e":"g","f":"h","g":"i","h":"j","i":"k","j":"l","k":"m","l":"n","m":"o",
				 "n":"p","o":"q", "p": "r","q":"s","r":"t","s":"u","t":"v","u":"w","v":"x","w":"y","x":"z"}
str_array = my_str.split(' ')
print(str_array)
str_array_trans = []
for i in str_array:
	s = []
	for j in i:
		s.append(alphabet_dict2[j]) if j in alphabet_dict2 else s.append(j)
	str_array_trans.append(''.join(s))

print(' '.join(str_array_trans))

#  简单的方法
from_str = 'abcdefghijklmnopqrstuvwxyz'
to_str = 'cdefghijklmnopqrstuvwxyzab'
transform = str.maketrans(from_str,to_str)
hints = my_str.translate(transform)
print(hints)
result = 'map.html'.translate(transform)
print(result)


