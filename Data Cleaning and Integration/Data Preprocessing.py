# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:22:14 2018

@author: Fahim
"""

import pandas as pd
import numpy as np

sheet = pd.read_excel('./Data/Data/Price_Data.xlsx', sheetname = 0)

item = sheet.Item.unique()
item2 = sheet.Item
print(item2)
item3 = item2.to_frame()

newdfallelectronics = []
newdfhightech = []
meanallelectronics = []
meanhightech = []

for i in range(len(item)):
    
    tempalle = []
    temphigh = []
    
    for j in range(len(sheet.Item)):
        
        if item[i] == sheet.Item[j]:
            
            tempalle.append(sheet.Price_AllElectronics[j])
            temphigh.append(sheet.Price_Hightech[j])
    
    #AllElectronics   
     
    ta = np.array(tempalle)
    medianall = np.nanmedian(ta, axis=0)
    indsa = np.where(np.isnan(ta))
    ta[indsa] = medianall
    meanallelectronics.append(ta.mean())
    df = pd.DataFrame(data=ta)
    newdfallelectronics.append(df)
  
    #Hightech
    
    th = np.array(temphigh)
    medianhigh = np.nanmedian(th, axis=0)
    indsh = np.where(np.isnan(th))
    th[indsh] = medianhigh
    meanhightech.append(th.mean())
    dfh = pd.DataFrame(data=th)
    newdfhightech.append(dfh)

print(meanallelectronics[0])
print(meanhightech)

dfg = pd.concat([newdfallelectronics[0], newdfallelectronics[1], newdfallelectronics[2], newdfallelectronics[3]], ignore_index=True)
print(dfg)
dfgf = pd.concat([newdfhightech[0], newdfhightech[1], newdfhightech[2], newdfhightech[3]], ignore_index=True)

merg = pd.merge(item3, dfg, left_index=True, right_index=True)
merged = pd.merge(merg, dfgf, left_index=True, right_index=True)
merged.columns = ['Item', 'Price_AllElectronics','Price_HighTech']
print(merged)
tempmeanallelectronics = []
tempmeanhightech = []

for i in range(24):
    if i <= 5:
        tempmeanallelectronics.append(meanallelectronics[0])
        tempmeanhightech.append(meanhightech[0])
    elif i <= 11 and i >= 6:
        tempmeanallelectronics.append(meanallelectronics[1])
        tempmeanhightech.append(meanhightech[1])
    if i <= 17 and i >= 12:
        tempmeanallelectronics.append(meanallelectronics[2])
        tempmeanhightech.append(meanhightech[2])
    elif i <= 23 and i >= 18:
       tempmeanallelectronics.append(meanallelectronics[3])
       tempmeanhightech.append(meanhightech[3])

meanalle = pd.DataFrame(data=tempmeanallelectronics)
meanhight = pd.DataFrame(data=tempmeanhightech)

merg1 = pd.merge(item3, meanalle, left_index=True, right_index=True)
merged1 = pd.merge(merg1, meanhight, left_index=True, right_index=True)
merged1.columns = ['Item', 'Price_AllElectronics','Price_HighTech']
print(merged1)

sumall = 0
sumht = 0
sophp = 0


for i in range(24):
    sumall = sumall + merged.Price_AllElectronics[i]
    sumht = sumht + merged.Price_HighTech[i]
    sophp = sophp + (merged.Price_AllElectronics[i] * merged.Price_HighTech[i])
        
temp = (sophp/24) - ((sumall/24)*(sumht/24))

if temp > 0:
    print("Price is rising together")
else:
    print("Price is falling together")
