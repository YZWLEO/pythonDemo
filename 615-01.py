#!/usr/bin/python
#coding=utf-8
import math
import os
from glob import glob
from platform import python_version

from PIL import Image

"""
png 转化
"""

def png2webp(inputFile,outputFile):
    try:
        image = Image.open(inputFile)
        #print image
        # if image.mode != 'RGBA' and image.mode != 'RGB':
        #     image = image.convert('RGBA')
        # image.save(outputFile,'WEBP')
        #image = image.convert('1');
        #image = image.filter(ImageFilter.BLUR)
        image.save(outputFile+'.jpeg')
        math.sqrt(4)
        print inputFile+' has converted to '+ outputFile
    except Exception as e:
        print "error"+e.message


print python_version();

matchFileList = glob('./png/*.png')

if len(matchFileList) <= 0:
    print("There are no *.png file in this directory (you can run this script in your *png directory)!")
    exit(-1)

outputDir = os.getcwd() + "/output"
print outputDir
print matchFileList
#exit(0)
for pngFile in matchFileList:
    fileName = pngFile[5:pngFile.index('.',1)]
    print pngFile+'#'+fileName
    #exit(0);
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    print pngFile+'#'+outputDir + "/" + fileName + ".webp"
    png2webp(pngFile, outputDir + "/" + fileName + ".webp")

print("Converted done! all webp file in the output directory!")
