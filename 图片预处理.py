#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:31:20 2018

@author: hujingyi
"""

from PIL import Image

#对图片进行预处理

for i in range(1,63):
	img=Image.open('/Users/hujingyi/Desktop/gift1/gift'+str(i)+'.png')
	#1280 × 960就是主图片的尺寸，我们将所有的图片修改为这一尺寸
	img=img.resize((960,1280)) 
	#每张不同的图片拷贝10份，拷贝多少份根据大家自身情况而定
	for j in range(10):
		img.save('/Users/hujingyi/Desktop/gift1/gift'+str(j*62+i)+'.png') #620 photos
        


