# coding: utf-8


import cv2 as ocv
import numpy as np 
import glob
import matplotlib.pyplot as plt


meanR = []
meanG = []
meanB = []
medianR = []
medianG = [] 
medianB = []
rangeR = []
rangeG = []
rangeB = []

imfolread = glob.glob("./Images/*.jpg")

i=-1
for img in imfolread:
    i+=1
    #temp = []
    print(img)
    image = ocv.imread(img)
    print(image.shape)
    b, r, g = ocv.split(image)
    bluechannel = np.array(b)
    bminval = bluechannel.min()
    bmaxval = bluechannel.max()
    brange = ((bmaxval-bminval)/2)
    rangeB.append(brange)
    bmean = bluechannel.mean()
    bmedian = np.median(bluechannel)
    meanB.append(bmean)
    medianB.append(bmedian)
    print("Mean Blue : "+str(bluechannel.mean()))
    print("Median Blue : "+str(np.median(bluechannel)))
    print("Range Blue : "+str(brange))
    redchannel = np.array(r)
    rminval = redchannel.min()
    rmaxval = redchannel.max()
    rrange = ((rmaxval-rminval)/2)
    rangeR.append(rrange)
    rmean = redchannel.mean()
    rmedian = np.median(redchannel)
    meanR.append(rmean)
    medianR.append(rmedian)
    print("Mean Red : "+str(redchannel.mean()))
    print("Median Red : "+str(np.median(redchannel)))
    print("Range Red : "+str(rrange))
    greenchannel = np.array(g)
    gminval = greenchannel.min()
    gmaxval = greenchannel.max()
    grange = ((gmaxval-gminval)/2)
    rangeG.append(grange)
    gmean = greenchannel.mean()
    gmedian = np.median(greenchannel)
    meanG.append(gmean)
    medianG.append(gmedian)
    print("Mean Green : "+str(greenchannel.mean()))
    print("Median Green : "+str(np.median(greenchannel)))
    print("Range Green : "+str(grange))
    

print(meanB)
print(meanR)
print(meanG)
print(medianB)
print(medianR)
print(medianG)
print(rangeB)
print(rangeR)
print(rangeG)
print(meanR[0]-meanR[1])


w, h = 15, 15;
meanRMat = [[0 for x in range(w)] for y in range(h)]
meanGMat = [[0 for x in range(w)] for y in range(h)]
meanBMat = [[0 for x in range(w)] for y in range(h)]
medianRMat = [[0 for x in range(w)] for y in range(h)]
medianGMat = [[0 for x in range(w)] for y in range(h)]
medianBMat = [[0 for x in range(w)] for y in range(h)]
rangeRMat = [[0 for x in range(w)] for y in range(h)]
rangeGMat = [[0 for x in range(w)] for y in range(h)]
rangeBMat = [[0 for x in range(w)] for y in range(h)]


count = 0
for i in range(0,15):
    for j in range((i+1),15):
        meanRMat[i][j] = abs(meanR[i]-meanR[j])
        meanGMat[i][j] = abs(meanG[i]-meanG[j])
        meanBMat[i][j] = abs(meanB[i]-meanB[j])
        medianRMat[i][j] = abs(medianR[i]-medianR[j])
        medianGMat[i][j] = abs(medianG[i]-medianG[j])
        medianBMat[i][j] = abs(medianB[i]-medianB[j])
        rangeRMat[i][j] = abs(rangeR[i]-rangeR[j])
        rangeGMat[i][j] = abs(rangeG[i]-rangeG[j])
        rangeBMat[i][j] = abs(rangeB[i]-rangeB[j])


print(count)
print(meanBMat)
print(meanRMat)
print(meanGMat)
print(medianBMat)
print(medianRMat)
print(medianGMat)
print(rangeBMat)
print(rangeRMat)
print(rangeGMat)


w, h = 15, 15;
finalAr = [[0 for x in range(w)] for y in range(h)]
for i in range(0, 15):
    for j in range(0,15):
        finalAr[i][j] = ((meanRMat[i][j] + meanGMat[i][j] + meanBMat[i][j] + medianRMat[i][j] + medianGMat[i][j] + medianBMat[i][j] + rangeRMat[i][j] + rangeGMat[i][j] + rangeBMat[i][j])/9)     

final = np.array(finalAr)

print(final)
ind = np.unravel_index(np.argmax(final , axis = None), final.shape)
print(ind)
print(ind[0])


for i in range(2):
    if ind[i] < 10:
        image = ocv.imread("./Images/30%d.jpg" % (ind[i]))
        plt.imshow(ocv.cvtColor(image, ocv.COLOR_BGR2RGB))
        plt.title("Image No : 30%d.jpg"%(ind[i]))
        plt.show()
    else:
        image = ocv.imread("./Images/3%d.jpg" % (ind[i]))
        plt.imshow(ocv.cvtColor(image, ocv.COLOR_BGR2RGB))
        plt.title("Image No : 3%d.jpg" % (ind[i]))
        plt.show()

