import os,sys
import Image

#   amount to trim off sides
trimL = 18
trimR = 154
trimT = 334
trimB = 19

imageFile = "dataSummary.png"
imageToResize = Image.open(imageFile)
w, h = imageToResize.size
imageToResize.crop((trimL, trimT, w-trimR, h-trimB)).save(imageFile)