import os,sys
import Image
#imageFile = "jsData.png"
#imageFile = "pythonData.png"
#imageFile = "cppData.png"
#imageFile = "javaData.png"
#imageFile = "rubyData.png"
imageFile = "qfactor.png"
imageToResize = Image.open(imageFile)
w, h = imageToResize.size
imageToResize.crop((170, 40, w-140, h-55)).save(imageFile)