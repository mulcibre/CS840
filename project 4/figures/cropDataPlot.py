#   Image Cropping Utility
#   Samuel Gluss
#   latest update 4-2-2016
#   added edge detection and auto cropping with out-of-bounds protection
#   Set padding around figure below:
padding = 10

import os,sys,glob,Image
#import pdb; pdb.set_trace()
    
# threshold is the minimum average pixel value considered to be non-white
# findX is true if scanning for an x value, false for finding y values
def getEdge(image, thresh, oBeg, oEnd, iBeg, iEnd, findX):
    inc = 1 if oBeg < oEnd else -1
    #   find edge
    for i in range(oBeg,oEnd, inc):
        for j in range(iBeg,iEnd):
            #   set pixel to correct coordinate based on scanning direction
            pixel = image.getpixel((i,j)) if findX else image.getpixel((j,i))
            #   if a non-white pixel is found, return value
            if (sum(pixel)/float(len(pixel))) < thresh:
                return i
        
#   find edges of image to crop
def findEdges(image, edges, imageWidth, imageHeight):
    imageWidth -= 1
    imageHeight -= 1
    #   maximum value considered to be non-white
    threshold = 250
    
    #   scan right to get left edge
    edges[0] = getEdge(image, threshold,0,imageWidth,0,imageHeight,True)
    #   scan left to get right edge
    edges[1] = getEdge(image, threshold,imageWidth,0,0,imageHeight,True)
    #   scan down to get top edge
    edges[2] = getEdge(image, threshold,0,imageHeight,0,imageWidth,False)
    #   scan up to get bottom edge
    edges[3] = getEdge(image, threshold,imageHeight,0,0,imageWidth,False)
    
    return edges

#   load all files in current directory with .png extension
imageFiles = []
for file in glob.glob("*.png"):
    imageFiles.append(file)

#   debug print    
print imageFiles
print

#   trim margins on each image
for image in imageFiles:
    imageToResize = Image.open(image)
    w, h = imageToResize.size
    #   edge left, right, top, bottom
    edges = [0,0,0,0]
    findEdges(imageToResize, edges, w, h)
    lCrop = edges[0] - padding
    rCrop = edges[1] + padding
    tCrop = edges[2] - padding
    bCrop = edges[3] + padding
    
    #   protect against out-of-bounds
    lCrop = lCrop if lCrop > 0 else 0
    rCrop = rCrop if rCrop < w else w
    tCrop = tCrop if tCrop > 0 else 0
    bCrop = bCrop if bCrop < h else h
    
    imageToResize.crop((lCrop, tCrop, rCrop, bCrop)).save(image)