# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 22:39:41 2018

@author: Fahim
"""

import pandas as pd
import numpy as np
import tkinter as tk

sheet = pd.read_excel('./Data/Data/Price_Data.xlsx', sheetname = 0)

item = sheet.Item.unique()
item2 = sheet.Item
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


dfg = pd.concat([newdfallelectronics[0], newdfallelectronics[1], newdfallelectronics[2], newdfallelectronics[3]], ignore_index=True)
dfgf = pd.concat([newdfhightech[0], newdfhightech[1], newdfhightech[2], newdfhightech[3]], ignore_index=True)

merg = pd.merge(item3, dfg, left_index=True, right_index=True)
merged = pd.merge(merg, dfgf, left_index=True, right_index=True)
merged.columns = ['Item', 'Price_AllElectronics','Price_HighTech']


tempmeanallelectronics = []
tempmeanhightech = []

for i in range(24):
    if i <= 5:
        tempmeanallelectronics.append(meanallelectronics[0])
        tempmeanhightech.append(meanhightech[0])
    elif i <= 11 and i >= 6:
        tempmeanallelectronics.append(meanallelectronics[1])
        tempmeanhightech.append(meanhightech[1])
    elif i <= 17 and i >= 12:
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

sumall = 0
sumht = 0
sophp = 0


for i in range(24):
    sumall = sumall + merged.Price_AllElectronics[i]
    sumht = sumht + merged.Price_HighTech[i]
    sophp = sophp + (merged.Price_AllElectronics[i] * merged.Price_HighTech[i])
        
convarience = (sophp/24) - ((sumall/24)*(sumht/24))


    
master = tk.Tk()
master.title('Data Mining')
master.geometry('1280x720')

msg = tk.Message(master,text="")
label = tk.Label(master, text="")
def OpenSheet():
    global msg
    global label
    #print(sheet)
    try:
        msg.pack_forget()
        label.pack_forget()
    except Exception:
        pass
    label = tk.Label(master, text="Showing Excel Sheet", bg="green", fg="black")
    label.pack()
    msg = tk.Message(master, text = sheet)
    
    msg.pack()
    
    #msg.pack_forget()
def MedianFill():
    global msg
    global label
    #print(merged)
    try:
        msg.pack_forget()
        label.pack_forget()
    except Exception:
        pass
    
    label = tk.Label(master, text="Filling Missing value with Median Attribute", bg="green", fg="black")
    label.pack()
    msg = tk.Message(master, text = merged)
    msg.pack()
    return merged


def NoiseReduce():
    #print(merged1)
    global msg
    global label
    try:
        msg.pack_forget()
        label.pack_forget()
    except Exception:
        pass
    
    label = tk.Label(master, text="Reducing Noise Using Bin Means", bg="green", fg="black")
    label.pack()
    msg = tk.Message(master, text = merged1)
    msg.pack()
    
    
def Convariance():
    global msg
    global label
    try:
        msg.pack_forget()
        label.pack_forget()
    except Exception:
        pass
    
    label = tk.Label(master, text="Calculating Covariance", bg="green", fg="black")
    label.pack()
    if convarience > 0:
        #print("Price is rising")
        message = "Price is rising"
        msg = tk.Message(master, text = message)
        msg.pack()
    else:
        #print("Price is falling")
        message = "Price is falling"
        msg = tk.Message(master, text = message)
        msg.pack()


def writetodirectory():
    global msg
    global label
    try:
        msg.pack_forget()
        label.pack_forget()
    except Exception:
        pass
    median = pd.ExcelWriter('./Data/Preprocessed data/Fillingmissingvalue.xlsx', engine='xlsxwriter')
    merged.to_excel(median, sheet_name='Sheet1')
    median.save()
    
    binmeans = pd.ExcelWriter('./Data/Preprocessed data/BinMeans.xlsx', engine='xlsxwriter')
    merged1.to_excel(binmeans, sheet_name='Sheet1')
    binmeans.save()
    
    label = tk.Label(master, text="Writing to directory as Excel", bg="green", fg="black")
    label.pack()
    msg = tk.Message(master, text = "Done")
    msg.pack()

b = tk.Button(master, text="Show Excel", command=OpenSheet)
b.pack(side="top", padx=4, pady=4)
b = tk.Button(master, text="Fill Missing", command=MedianFill)
b.pack(side="top", padx=4, pady=4)
b = tk.Button(master, text="Noise Remove", command=NoiseReduce)
b.pack(side="top", padx=4, pady=4)
b = tk.Button(master, text="Covariance", command=Convariance)
b.pack(side="top", padx=4, pady=4)
b = tk.Button(master, text="Write Excel", command=writetodirectory)
b.pack(side="top", padx=4, pady=4)
 
tk.mainloop()
