#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 14:27:00 2018

@author: hujingyi
"""
from PIL import Image

# 生成背景图片
back_num=24  #576   1280 × 960
back_size=(back_num*960,back_num*1280) #计算背景图尺寸
toimage=Image.new('RGBA',back_size)   #生成一张大小与背景图相同的白色图层
for i in range(1,577):
	fromimage=Image.open('/Users/hujingyi/Desktop/gift1/gift'+str(i)+'.png')
	#将576张照片依次贴在其对应位置
	toimage.paste(fromimage,(int((i-1)%back_num*960),int((i-1)/back_num*1280)))
toimage.save('/Users/hujingyi/Desktop/background3.png')

