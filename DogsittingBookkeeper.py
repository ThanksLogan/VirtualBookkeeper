
#from pyxll import xl_func
import pandas as pd
import numpy as np
from collections import defaultdict
import datetime
print("...program starting...")
#Dee is the variable name of our workbook
#Dee = load_workbook('arg1')

df = pd.read_excel('/Users/loganforeman/Desktop/Python prod/DogsittingBook.xlsx') 
def getAllCusIDBookings(df):
    cusIDBookings = defaultdict(list)
    cusIDListRaw = {}
    bookingLineList = []
    for i in range(len(df.index)):
        name1 = df.loc[i, "Name"]  #get name 
        firstChar = name1[0] 
        secondChar = name1[1]
        thirdChar = name1[3]
        intCode = (ord(firstChar) * ord(secondChar) * ord(thirdChar)) //111 #hash function 
        #create list from line 
        date = df.loc[i, "Date"]
        name = df.loc[i, "Name"] #name of person
        total = df.loc[i, "numCost"]
        nightly = df.loc[i, "Nightly/$"]
        numDogs = df.loc[i, "numDogs"]
        numHolidays = df.loc[i, "numHolidays"]
        distance = df.loc[i, "Distance"]
        payMethod = df.loc[i, "PaymentMode"]
        walkCost = df.loc[i, "walkPayment"]
        #add list to dict where the key is the intCode 
        bookingLineList.append(name)
        bookingLineList.append(date)
        bookingLineList.append(total)
        bookingLineList.append(nightly)
        bookingLineList.append(numDogs)
        bookingLineList.append(numHolidays)
        bookingLineList.append(distance)
        bookingLineList.append(payMethod)
        bookingLineList.append(walkCost)
        iBookingLineList = []
        iBookingLineList = iBookingLineList + bookingLineList 
    #print(bookingLineList)
        cusIDBookings[intCode].extend(iBookingLineList)
        cusIDBookings[intCode].extend("\n")
        bookingLineList.clear()
        iBookingLineList.clear()
    return cusIDBookings
class HashTable:

  
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
  
    def create_buckets(self):
        return [[] for _ in range(self.size)]
  
    # Insert values into hash map
    def set_val(self, key, val):
        
        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break
  
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
  
    # Return searched value with specific key
    def get_val(self, key):
        
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as 
            # the key being searched
            if record_key == key:
                found_key = True
                break
  
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"
  
    # Remove a value with specific key
    def delete_val(self, key):
        
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
          
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
  
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
              
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
  
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

#needs to also handle putting all the info about a customer into the hash table
def getBookingsByID(df):
    data = []
    nameList = []
    combinedDataList = {}
    for index in range(len(df.index)):
        dataList = {} #list of all the info for each line 
        #hashingmethod for cusID 
        
        date = df.loc[index, "Date"]
        name3 = df.loc[index, "Name"] #name of person
        total = df.loc[index, "numCost"]
        nightly = df.loc[index, "Nightly/$"]
        numDogs = df.loc[index, "numDogs"]
        numHolidays = df.loc[index, "numHolidays"]
        distance = df.loc[index, "Distance"]
        payMethod = df.loc[index, "PaymentMode"]
        walkCost = df.loc[index, "walkPayment"]
        #~~~~~CustomHASH
        firstChar = name3[0] 
        secondChar = name3[1]
        thirdChar = name3[3]
        intCode2 = (ord(firstChar) * ord(secondChar) * ord(thirdChar)) //111 #hash function 
        #~~~~~~~~~~~~~~~
        dataList.update({0: intCode2})
        dataList.update({1: name3})
        dataList.update({2: date})
        dataList.update({3: total})
        dataList.update({4: nightly})
        dataList.update({5: numDogs})
        dataList.update({6: numHolidays})
        dataList.update({7: distance})
        dataList.update({8: payMethod})
        dataList.update({9: walkCost})
        #datalist:
        #{0: 'Andrea', 1: Timestamp('2022-01-07 00:00:00'), 2: nan, 3: nan, 4: nan, 5: nan, 6: 4.4, 7: 'venmo', 8: 15.0}
        nameList.append(name3)
        combinedDataList[index] = dataList
        #print(data[index])
    #since there are more lines than nameList, if name in datalist matches namelist, add it to that portion of hashtable
    #generate unique customer id for each line in namelist
    #name_List.sort()
    #temp = defaultdict(lambda: len(temp))
    #idList = [temp[ele] for ele in nameList]
    #for i in range(len(idList)):
    #    hash_table.set_val(idList[i], nameList[i])
    #    if(data[i][0]==nameList[i]):
    #       print(data[i][0])
    #       hash_table.set_val(idList[i], data[i])
    return combinedDataList

#hash_table = HashTable(len(df.index))
listOfBookings = getBookingsByID(df)
for id, value in listOfBookings.items():
        print("\nID:", value[0])
    
        for key in value:
            print(str(key) + ':', value[key])
#the next part of this needs to handle the parts on the sheet that
def getBookingsByDate(df):
    print("hello", '\n')
    data = []
    nameList = []
    combinedDataList = {}
    for index in range(len(df.index)):
        dataList = {} #list of all the info for each line 
        #hashingmethod for cusID 
        
        date = df.loc[index, "Date"]
        name3 = df.loc[index, "Name"] #name of person
        total = df.loc[index, "numCost"]
        nightly = df.loc[index, "Nightly/$"]
        numDogs = df.loc[index, "numDogs"]
        numHolidays = df.loc[index, "numHolidays"]
        distance = df.loc[index, "Distance"]
        payMethod = df.loc[index, "PaymentMode"]
        walkCost = df.loc[index, "walkPayment"]
        #~~~~~CustomHASH
        firstChar = name3[0] 
        secondChar = name3[1]
        thirdChar = name3[3]
        intCode2 = (ord(firstChar) * ord(secondChar) * ord(thirdChar)) //111 #hash function 
        #~~~~~~~~~~~~~~~
        dataList.update({0: intCode2})
        dataList.update({1: name3})
        dataList.update({2: date})
        dataList.update({3: total})
        dataList.update({4: nightly})
        dataList.update({5: numDogs})
        dataList.update({6: numHolidays})
        dataList.update({7: distance})
        dataList.update({8: payMethod})
        dataList.update({9: walkCost})
        #datalist:
        #{0: 'Andrea', 1: Timestamp('2022-01-07 00:00:00'), 2: nan, 3: nan, 4: nan, 5: nan, 6: 4.4, 7: 'venmo', 8: 15.0}
        nameList.append(name3)
        combinedDataList[date] = dataList
        #print(data[index])
    #since there are more lines than nameList, if name in datalist matches namelist, add it to that portion of hashtable
    #generate unique customer id for each line in namelist
    #name_List.sort()
    #temp = defaultdict(lambda: len(temp))
    #idList = [temp[ele] for ele in nameList]
    #for i in range(len(idList)):
    #    hash_table.set_val(idList[i], nameList[i])
    #    if(data[i][0]==nameList[i]):
    #       print(data[i][0])
    #       hash_table.set_val(idList[i], data[i])
    return combinedDataList

def getGasData(cusID):
    #first, obtain distance(in miles): (data[cusID][6])
    #second, utilize mpg of my toyota matrix which is 25mpg city
    #third, do distance / 25mpg = gallons needed for trip to house
    #lastly, use current price of gas @ $5.50 to calculate price: price = (5.5(distance/25)
    #** on average 1 trip home per night of the dogsit: numNights(5.5(2*distance/25)
    #cusID = data[cusID] #should be a\ line from list 
    print("hello")
    pricePerNight = data[cusID][2]/data[cusID][3]
    distance = data[cusID][6]
    totalGasPriceForStay = pricePerNight(5.5(2*(distance)/25))
    return ("Estimated total cost of gas is: $",totalGasPriceForStay)

def convertDatetoDay(date):
    #date is in form YYYY-MM-DD 00:00:00
    #we will parse date in string form
    #len=10, index 0,1,2,3 = YYYY, 5,6=MM, 8,9=DD
    strDate = str(date)
    #intDate = int(str[0:3:1])
    year = int(strDate[0:4:1])
    month = int(strDate[5:7:1])
    day =int(strDate[8:10:1])
    d = datetime.datetime(year, month, day)
    #+ strDate[8:9]
    return(d)

def getQuarterlyEarnings(Q):
    #using data, this will compute the total cost added together for each quarter based on dates
    data = getBookingsByDate(df)
    #TODO: create markers which can denote the quarter based on timestamp of hashtable
    #choose quarter: Q1, Q2, Q3, Q4
    #Q1
    #val = input("Type Quarter in form 'Q1' : ")
    if(Q == "Q1"):
        i=0
        dogsitRevenueQ1 = 0.0
        dogwalkRevenueQ1 = 0.0
        for i in data:
            dateq1 = convertDatetoDay(data[i][2])
            if(datetime.datetime(2022, 3, 31)>dateq1):
                dogsitRevenueCell= float(data[i][3])
                dogwalkRevenueCell = float(data[i][9])
                if (dogsitRevenueCell > 0):
                    dogsitRevenueQ1 += dogsitRevenueCell
                elif (dogwalkRevenueCell > 0):
                    dogwalkRevenueQ1 += dogwalkRevenueCell
            else:
                break
        totalQ1 = dogsitRevenueQ1 + dogwalkRevenueQ1
        return("Quarterly Earnings:", Q, " -dogsitRevenue:",dogsitRevenueQ1," -dogwalkRevenue: ", dogwalkRevenueQ1," -TOTAL: ", totalQ1)
    elif(Q == "Q2"):
        i=0
        dogsitRevenueQ2 = 0.0
        dogwalkRevenueQ2 = 0.0
        for i in data:
            dateq2 = convertDatetoDay(data[i][2])
            if(datetime.datetime(2022, 7, 1) > dateq2 and datetime.datetime(2022, 3, 31)<dateq2):
                    dogsitRevenueCell= float(data[i][3])
                    dogwalkRevenueCell = float(data[i][9])
                    if (dogsitRevenueCell >0):
                        dogsitRevenueQ2+= dogsitRevenueCell
                    elif (dogwalkRevenueCell >0):
                        dogwalkRevenueQ2+= dogwalkRevenueCell
        
        totalQ2 = dogsitRevenueQ2 + dogwalkRevenueQ2
        return("Quarterly Earnings:", Q, " -dogsitRevenue:",dogsitRevenueQ2," -dogwalkRevenue: ", dogwalkRevenueQ2," -TOTAL: ", totalQ2)
    elif(Q == "Q3"):
        i=0
        dogsitRevenueQ3 = 0.0
        dogwalkRevenueQ3 = 0.0
        for i in data:
            dateq3 = convertDatetoDay(data[i][2])
            if(datetime.datetime(2022, 10, 1) > dateq3 and datetime.datetime(2022, 6, 30) < dateq3):
                    dogsitRevenueCell= float(data[i][3])
                    dogwalkRevenueCell = float(data[i][9])
                    if (dogsitRevenueCell >0):
                        dogsitRevenueQ3+= dogsitRevenueCell
                    elif (dogwalkRevenueCell >0):
                        dogwalkRevenueQ3+= dogwalkRevenueCell
        
        totalQ3 = dogsitRevenueQ3 + dogwalkRevenueQ3
        return("Quarterly Earnings:", Q, " -dogsitRevenue:",dogsitRevenueQ3," -dogwalkRevenue: ", dogwalkRevenueQ3," -TOTAL: ", totalQ3)
    elif(Q == "Q4"):
        i=0
        dogsitRevenueQ4 = 0.0
        dogwalkRevenueQ4 = 0.0
        for i in data:
            dateq4 = convertDatetoDay(data[i][2])
            if(datetime.datetime(2022, 12, 31) > dateq4 and datetime.datetime(2022, 9, 30) < dateq4):
                    dogsitRevenueCell= float(data[i][3])
                    dogwalkRevenueCell = float(data[i][9])
                    if (dogsitRevenueCell >0):
                        dogsitRevenueQ4+= dogsitRevenueCell
                    elif (dogwalkRevenueCell >0):
                        dogwalkRevenueQ4+= dogwalkRevenueCell
        
        totalQ4 = dogsitRevenueQ4 + dogwalkRevenueQ4
        return("Quarterly Earnings:", Q, " -dogsitRevenue:",dogsitRevenueQ4," -dogwalkRevenue: ", dogwalkRevenueQ4," -TOTAL: ", totalQ4)
    else:
        return("that is not a valid quarter, please input as 'Q#' form")

val = input("Type Quarter in form 'Q1' : ")
if(val!= "Q1" or val!= "Q2" or val!= "Q3" or val!="Q4"):
    print("that is not a valid quarter, please input as 'Q#' form")
    print("please try again")
    val = input("Type Quarter in form 'Q#' : ")
print(getQuarterlyEarnings(val))


def TestDogsitPrice(numNights, numDogs, distance, numHolidays, numRate):
    #userprompt here 
    # select: numNights, numDogs, distance, numRate, etc.
    #nights = input("Please enter the number of Nights: ")
    totalCost = numNights * (numDogs * numRate)

