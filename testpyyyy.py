#this is the file for my shii cuhhh
#from pyxll import xl_func
import pandas as pd
import numpy as np
from collections import defaultdict
print("Hello my ninja ")
#Dee is the variable name of our workbook
#Dee = load_workbook('arg1')

df = pd.read_excel('/Users/loganforeman/Desktop/Python prod/DogsittingBook.xlsx') 

    cusIDBookings = {}
    bookingLineList = []
    #for index in range(len(df.index)):
       # name2 = df.loc[index, "Name"]  #get name 
        #firstChar2 = name2[0] 
       # secondChar2 = name2[1]
        #thirdChar2 = name2[3]
        #intCode2 = (ord(firstChar2) + ord(secondChar2) + ord(thirdChar2)) * 12 #hash function 
        #cusIDBookings[intCode2]
    for index in range(len(df.index)):
        name1 = df.loc[index, "Name"]  #get name 
        firstChar = name1[0] 
        secondChar = name1[1]
        thirdChar = name1[3]
        intCode = (ord(firstChar) + ord(secondChar) + ord(thirdChar)) * 12 #hash function 
        #create list from line 
        date = df.loc[index, "Date"]
        name = df.loc[index, "Name"] #name of person
        total = df.loc[index, "numCost"]
        nightly = df.loc[index, "Nightly/$"]
        numDogs = df.loc[index, "numDogs"]
        numHolidays = df.loc[index, "numHolidays"]
        distance = df.loc[index, "Distance"]
        payMethod = df.loc[index, "PaymentMode"]
        walkCost = df.loc[index, "walkPayment"]
        #add list to dict where the key is the intCode 
        bookingLineList.append(date)
        bookingLineList.append(name)
        bookingLineList.append(total)
        bookingLineList.append(nightly)
        bookingLineList.append(numDogs)
        bookingLineList.append(numHolidays)
        bookingLineList.append(distance)
        bookingLineList.append(payMethod)
        bookingLineList.append(walkCost)
        #cusIDBookings[intCode] += (bookingLineList)
        cusIDBookings.setdefault(intCode, []).append(bookingLineList)
    for value in cusIDBookings.values():
        print(value)
    #return cusIDBookings
