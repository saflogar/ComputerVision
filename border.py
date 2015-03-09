from PIL import Image
from pylab import *
from numpy import *
import sys
import getopt
import os
import string 
import pdb
from decimal import *

def readImage(imageName):
    im = array(Image.open(imageName).convert('L'))
    return im

def medianFilter(imString):    
    im = readImage(imString)
    lx = len(im)
    ly = len (im[0])
    mLen = 3
    mWid = 3
    newIm = Image.new("RGB",(ly,lx),"white")
    newImArr = arange(im.size,dtype=np.uint8).reshape(lx,ly)    
    print "[DEBUG] lx = ",lx, "ly = ",ly                
    for x in range (lx-1):
        for y in range (ly-1):
            hist = [0 for i in range(256)]
            neighList = [0 for i in range(mLen)]
            for i in range (mLen):
                suma = 0
                for j in range (mWid):
                    ii = (x-1)+i
                    jj = (y-1)+j
                    if ii >= 0 and jj >= 0 and jj < ly and ii < lx:
                        hist[im[ii][jj]] += 1
                        neighList.append(im[ii][jj])
#                        neighList[]                   
            sorHist = bubbleSort(neighList)
#           print sorHist
            newImArr[x][y] = sorHist[4]
#           pdb.set_trace()
#           newIm = Image
#           pdb.set_trace()
    newIm = Image.fromarray(newImArr,'L')

    test = Image.fromarray(im,'L')
    test.save("test.jpg")
    newIm.save("median.jpg")    

def bubbleSort(sortList):    
    cont = 1
    while cont != 0:        
        cont = 0
        for i in range(len(sortList)-1):
            if sortList[i] < sortList[i+1]:
                a = sortList[i]
                b = sortList[i+1]
                sortList[i]  = b
                sortList[i+1]= a
                cont = 1
#    print sortList
    return sortList
                                       
def convelve (mask,imString):
    im = readImage(imString)
#    mask = [[0,-1,0],[-1,5,-1],[0,-1,0]]
#    mask = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
#    mask = [[1,1,1],[1,1,1],[1,1,1]] #Gaussian *Remember divide between 9 each 
#    pdb.set_trace()

    lx = len(im)
    ly = len (im[0])
    mLen = len(mask[0])
    mWid = len(mask[0][0])
  
    newIm = Image.new("RGB",(ly,lx),"white")
    newImArr = arange(im.size,dtype=np.uint8).reshape(lx,ly)
    print "[DEBUG] lx = ",lx, "ly = ",ly

    for x in range (lx-1):
        for y in range (ly-1):
            total = 0   
            #newImArr[x][y] = im[x][y]
            v = 0
            pixelGrads = [0 for i in range(8)]
            for m in mask:
                m.reverse()                
                for i in range (mLen):
                    suma = 0
                    for j in range (mWid):
                        ii = (x-1)+i
                        jj = (y-1)+j         
                        if ii >= 0 and jj >= 0 and jj < ly and ii < lx:
                        #suma = im[ii][jj] * (mask[i][j] / float(9) )
                            suma = im[ii][jj] * m[i][j]
                            pixelGrads[v] = pixelGrads[v]+ suma
                            total += suma   
                v=v+1
                newImArr[x][y] = max(pixelGrads)
            
            
    newIm = Image.fromarray(newImArr,'L')
    test = Image.fromarray(im,'L')
    test.save("test.jpg")
    newIm.save("gaussianConv.jpg")
masks = [[-1,1,1],[-1,-2,1],[-1,1,1]],[[1,1,1],[1,-2,1],[-1,-1,1]],[[1,1,1],[1,-2,1],[-1,-1,-1]],[[1,1,1],[1,-2,-1],[1,-1,-1]]
#for i in range(len(masks)):
#mask = [[1,1,1],[1,1,1],[1,1,1]]#gaussian
mask = [[-1,-2,-1],[0,0,0],[1,2,1]]
#medianFilter('median.jpg')

medianFilter('erp.jpg')
convelve(masks,'median.jpg')
#convelve(masks[3],'empire.jpg')
        

