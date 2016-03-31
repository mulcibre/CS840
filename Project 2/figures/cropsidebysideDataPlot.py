import os,sys,glob,Image
#import pdb; pdb.set_trace()

#   how much to crop from sides/top
leftChop = 145
rightChop = 145
topChop = 45
BottomChop = 45

#   Where to begin and stop removing columns
sliceStart = 870
sliceEnd = 950
diff = sliceEnd - sliceStart

#   load all files in current directory with .png extension
imageFiles = []
for file in glob.glob("*.png"):
    imageFiles.append(file)

#   debug print    
print imageFiles
print

for image in imageFiles:
    #   open source image and get dimensions
    imageToResize = Image.open(image)
    w, h = imageToResize.size
    
    #   create new workspace to paste crops into
    im = Image.new("RGB", (w - (leftChop + rightChop + diff), h - (topChop + BottomChop)))
    offset = 0;
    
    #   paste left crop
    im.paste(imageToResize.crop((leftChop, topChop, w-(rightChop+diff), h-BottomChop)),(0,0))
    offset += sliceStart - leftChop
    
    #   paste right crop
    im.paste(imageToResize.crop((sliceEnd, topChop, w-rightChop, h-BottomChop)),(offset,0))
    
    #   save modified image
    im.save(image)