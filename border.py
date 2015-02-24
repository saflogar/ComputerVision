from PIL import Image
from pylab import *
from numpy import *
import sys
import getopt
import os
import string 
import pdb

def readImage(imageName):
    im = array(Image.open(imageName).convert('L'))
    return im

def convelve ():
    im = readImage('figuras.jpg')
    mask = [[0,-1,0],[-1,5,-1],[0,-1,0]]
#    mask = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
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
    pdb.set_trace()
    newIm = Image.fromarray(newImArr,'L')
    test = Image.fromarray(im,'L')
    test.save("test.jpg")
    newIm.save("convelved.jpg")
convelve()        
