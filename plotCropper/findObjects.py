#   Image Cropping Utility
#   Samuel Gluss
#   latest update 4-2-2016
#   added edge detection and auto cropping with out-of-bounds protection
#   Set padding around figure below:

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
print(imageFiles)
print

#   trim margins on each image
for image in imageFiles:
    imageToResize = Image.open(image)
    w, h = imageToResize.size

    thresh = 250
    #   padding to add between objects
    padding = 10
    #   sensitivity determines how many whitespaces to read after the end of an object
    #   This ensures that labels correctly stay with their plots, ect...
    sensitivity = 20

#find horizontal objects
    horObjEdges = []
    readingObject = False
    whiteCol = True
    left = -1
    right = -1
    stillObject = sensitivity
    for i in range(0,w):
        whiteCol = True
        for j in range(0,h):
            pixel = imageToResize.getpixel((i, j))
            #   if a non-white pixel is found
            if (sum(pixel) / float(len(pixel))) < thresh:
                whiteCol = False
                if left == -1:
                    #reading first col of object
                    left = i
                    right = i
                else:
                    #already reading an object
                    right = i
                readingObject = True
                stillObject = sensitivity
                break
            #   made it to this point, col was all white
        if readingObject:
            if whiteCol:
                stillObject -= 1
            if stillObject <= 0 or i == w:
                #   commit found object, prepare to find new object
                horObjEdges.append([left,right])
                left = -1
                right = -1
                readingObject = False

#imageToResize.crop((lCrop, tCrop, rCrop, bCrop)).save(image)