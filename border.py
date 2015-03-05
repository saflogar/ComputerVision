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

def medianFilter():
    im = readImage('empire.jpg')
    lx = len(im)
    ly = len (im[0])
    mLen = 3
    mWid = 3

    newIm = Image.new("RGB",(ly,lx),"white")
    newImArr = arange(im.size,dtype=np.uint8).reshape(lx,ly)    
    print "[DEBUG] lx = ",lx, "ly = ",ly                
    for x in range (lx-1):
        for y in range (ly-1):               
            hist = [0 for i in range(255)]
            for i in range (mLen):
                suma = 0
                for j in range (mWid):
                    ii = (x-1)+i
                    jj = (y-1)+j         
                    if ii >= 0 and jj >= 0 and jj < ly and ii < lx:
                        hist[im[ii][jj]] += 1
            sorHist = bubbleSort(hist) 
            pdb.set_trace()
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
    return sortList
        

            
            
           
def convelve (mask):
    im = readImage('convelved.jpg')
#    mask = [[0,-1,0],[-1,5,-1],[0,-1,0]]
#    mask = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
#    mask = [[1,1,1],[1,1,1],[1,1,1]] Gaussian *Remember divide between 9 each 
#    pdb.set_trace()
    lx = len(im)
    ly = len (im[0])
    mLen = len(mask)
    mWid = len(mask[0])
    mask.reverse()
    newIm = Image.new("RGB",(ly,lx),"white")
    newImArr = arange(im.size,dtype=np.uint8).reshape(lx,ly)
    print "[DEBUG] lx = ",lx, "ly = ",ly
 #   pdb.set_trace()
    for x in range (lx-1):
        for y in range (ly-1):
            total = 0   
            #newImArr[x][y] = im[x][y]
            for i in range (mLen):
                suma = 0
                for j in range (mWid):
                    ii = (x-1)+i
                    jj = (y-1)+j         
                    if ii >= 0 and jj >= 0 and jj < ly and ii < lx:
                        suma = im[ii][jj] * mask[i][j] 
                        #print "total[",x,"]""[",y,"] = im[",ii,"][",jj,"] * mask[",i,"][",j,"]=",suma
                        total += suma                     
                        
 #           print total ,"in [",x,"][",y,"]"
#            print "x=",x,"y=",y
            newImArr[x][y] = total
#    pdb.set_trace()
    newIm = Image.fromarray(newImArr,'L')
    test = Image.fromarray(im,'L')
    test.save("test.jpg")
    newIm.save("convelved.jpg")

#masks = [[-1,1,1],[-1,-2,1],[-1,1,1]],[[1,1,1],[1,-2,1],[-1,-1,1]],[[1,1,1],[1,-2,1],[-1,-1,-1]],[[1,1,1],[1,-2,-1],[1,-1,-1]]
#masks[1] = [[1,1,1],[1,-2,1],[-1,-1,1]]
#masks[2] = [[1,1,1],[1,-2,1],[-1,-1,-1]]
#masks[3] = [[1,1,1],[1,-2,-1],[1,-1,-1]]
#pdb.set_trace()
#for i in range(len(masks)):
#convelve(masks[3])        
medianFilter()
