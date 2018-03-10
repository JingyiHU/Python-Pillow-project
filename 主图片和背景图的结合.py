#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 14:47:14 2018

@author: hujingyi
"""
from PIL import Image
Image.MAX_IMAGE_PIXELS = 1000000000 

# 将主图片与背景图片对应像素加权融合
content=Image.open('/Users/hujingyi/Desktop/photo2/9.png') #打开主图片
#将主图片resize成预定大小
content=content.resize((4800,6400))  
background=Image.open('/Users/hujingyi/Desktop/background3.png')
#这里对背景图尺寸进行调整是由于背景图过大，这样处理能够减少计算时间
background=background.resize((4800,6400))  
height=4800
width=6400
#新建一张新的图片
newimg=Image.new('RGBA',(4800,6400))
#对两张尺寸大小相等的图片进行遍历
for i in range(height):
	for j in range(width):
		a=content.getpixel((i,j))
		b=background.getpixel((i,j))
		#对应像素点的rgb值加权求和
		r=int (0.5*a[0]+0.5*b[0])
		g=int (0.5*a[1]+0.5*b[1])
		b=int (0.5*a[2]+0.5*b[2])
		newimg.putpixel((i,j),(r,g,b))
#将生成的图片保存起来
newimg.save('/Users/hujingyi/Desktop/final_lie4.png')

