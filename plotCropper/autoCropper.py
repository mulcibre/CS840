#   Image Cropping Utility
#   Samuel Gluss
#   latest update 4-2-2016
#   added edge detection and auto cropping with out-of-bounds protection
#   Set padding around figure below:

import os,sys,glob,Image
import pdb; pdb.set_trace()
    
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
    padding = 10
    
    #   find limits of whitespace cols
    horSpaces = []
    left = 0
    right = 0
    for i in range(0,w):
        isWhite = True
        for j in range(0,h):
            #   check pixel value, determine if it is white or not
            pixel = imageToResize.getpixel((i,j))
            notWhite = (sum(pixel)/float(len(pixel))) < thresh
            if notWhite:
                #found a limit, save whitespace block if bigger than padding
                if right - left > padding:
                    horSpaces.append([left,right])
                #   reset markers/flag to to search for next whitespace
                right = -1
                left = -1
                isWhite = False
                break
        if isWhite:
            #   encountered new whitespace, begin tracking
            if left == -1:
                left = i
                right = i
            else:
            #   encountered existing whitespace, increment cursor
                right += 1
            if i == w - 1:
                #   on last col, add whitespace if appropriate
                if right - left > padding:
                    horSpaces.append([left,right])
         
    #   find limits of whitespace rows
    vertSpaces = []
    upper = 0
    lower = 0
    for j in range(0,h):
        isWhite = True
        for i in range(0,w):
            pixel = imageToResize.getpixel((i,j))
            notWhite = (sum(pixel)/float(len(pixel))) < thresh
            if notWhite:
                #found a limit, save whitespace if bigger than padding
                if lower - upper > padding:
                    vertSpaces.append([upper,lower])
                lower = -1
                upper = -1
                isWhite = False
                break
        if isWhite:
            if upper == -1:
                upper = j
                lower = j
            else:
                lower += 1
            if j == h - 1:
                if lower - upper > padding:
                    vertSpaces.append([upper,lower])
                    
print horSpaces
print vertSpaces
#imageToResize.crop((lCrop, tCrop, rCrop, bCrop)).save(image)