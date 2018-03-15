#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs Mar  15 22:33:14 2018

@author: Inokinoki
"""
from PIL import Image
import random
import os

# Generate background image
def generate_blank_background(width, height):
    """	Generate a blank image as the background """
    background_size = (width, height)
    return Image.new('RGBA', background_size)   # Generate a layer filled with white
    

def mix(background_image, main_image, width, height, weight):
    """ Mix background and content with weight """
    main_image = main_image.resize((width, height))	# Resize main_image
    newimg = Image.new('RGBA', (width, height))

    # Mix with weight
    for i in range(width):
        for j in range(height):
            a = main_image.getpixel((i, j))
            b = background_image.getpixel((i, j))
            r = int (weight * a[0] + (1 - weight) * b[0])
            g = int (weight * a[1] + (1 - weight) * b[1])
            b = int (weight * a[2] + (1 - weight) * b[2])
            newimg.putpixel((i, j), (r, g, b))
    
    return newimg


def generate_content(image_lists, width, height, width_count, height_count):
    background = generate_blank_background(width, height)
    
    images = []
    
    for image_name in image_lists:
        # Need a strategy to handle resize ratio
        img = Image.open(image_name)
        img = img.resize((int(width / width_count), int(height / height_count))) 
        images.append(img)
        
    for i in range(0, width_count * height_count):
        # Paste
        background.paste(random.choice(images), (int(width / width_count * (i % width_count)),
            int(height / height_count * int(i / height_count))))
        
    return background
    
    
def getimages(path):
    """ Search all image files in current directory """
    files = os.listdir(path)
    list = []
    for file in files:
        if not os.path.isdir(file):
            if file.split(".")[-1].lower() == "png":
                list.append(path + "/" + file)
            elif file.split(".")[-1].lower() == "jpg":
                list.append(path + "/" + file)
            elif file.split(".")[-1].lower() == "jpeg":
                list.append(path + "/" + file)
        else:
            if file != "background":
                list.extend(getimages(file))
    return list
        

if __name__ == "__main__":
    # Get images for content and background
    lists = getimages("./")
    backgrounds = getimages("./background")
    if len(backgrounds) < 1 or len(lists) < 32:
        print("Usage: python pixelization.py")
        print("								")
        print("Please ensure you have ./background/xxx.(png|jpg|jpeg) as background")
        print("and more than 32 images as content generator in current directory.")
        print("								")
        print("请确认您有 ./background/xxx.(png|jpg|jpeg) 来作为图像的背景")
        print("和超过32张作为内容的图片在当前文件夹或子文件夹中")
        exit()

    Image.MAX_IMAGE_PIXELS = 1000000000 
    
    # Open background image
    print("Opening background image")
    image = Image.open(backgrounds[0])
    
    width, height = image.size
    
    print("Generating content image")
    content = generate_content(lists, width, height, 10, 10)
    
    print("Mixing images")
    dest_image = mix(image, content, width, height, 0.5)
    
    print("Finishing")
    dest_image.save("output.png")
    
