#this is the file for my shii cuhhh
#from pyxll import xl_func
import pandas as pd
import numpy as np
from collections import defaultdict
print("...program starting...                                       :)")
#Dee is the variable name of our workbook
#Dee = load_workbook('arg1')

df = pd.read_excel('/Users/loganforeman/Desktop/Python prod/DogsittingBook.xlsx') 

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
def parseSheet(HashTable):
    print("hello", '\n')
    data = []
    nameList = []
    data_list = {}
    for index in range(len(df.index)):
        dataList = {} #list of all the info for each line 
        #hashingmethod for cusID 
        
        date = df.loc[index, "Date"]
        name = df.loc[index, "Name"] #name of person
        total = df.loc[index, "numCost"]
        nightly = df.loc[index, "Nightly/$"]
        numDogs = df.loc[index, "numDogs"]
        numHolidays = df.loc[index, "numHolidays"]
        distance = df.loc[index, "Distance"]
        payMethod = df.loc[index, "PaymentMode"]
        walkCost = df.loc[index, "walkPayment"]
        #~~~~~CustomHASH
        firstChar = name[0]
        secondChar = name[1]
        intCode = (ord(firstChar) + ord(secondChar)) * 12
        #~~~~~~~~~~~~~~~
        dataList.update({0: intCode})
        dataList.update({1: name})
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
        nameList.append(name)
        data.append(dataList)
        #print(data[index])
    #since there are more lines than nameList, if name in datalist matches namelist, add it to that portion of hashtable
    #generate unique customer id for each line in namelist
    #name_List.sort()
    bigData = {}
    for j in range(len(df.index)):
        bigData.update({data[j][0]: data[j]})
    for id, value in bigData.items():
        print("\nID:", id)
    
        for key in value:
            print(str(key) + ':', value[key])
    
    temp = defaultdict(lambda: len(temp))
    idList = [temp[ele] for ele in nameList]
    for i in range(len(idList)):
        hash_table.set_val(idList[i], nameList[i])
        if(data[i][0]==nameList[i]):
           print(data[i][0])
           hash_table.set_val(idList[i], data[i])
    return HashTable

hash_table = HashTable(len(df.index))
cusIDs = parseSheet(hash_table)
print(cusIDs)
#the next part of this needs to handle the parts on the sheet that

def getGasData(cusID):
    #first, obtain distance(in miles): (data[cusID][6])
    #second, utilize mpg of my toyota matrix which is 25mpg city
    #third, do distance / 25mpg = gallons needed for trip to house
    #lastly, use current price of gas @ $5.50 to calculate price: price = (5.5(distance/25)
    #** on average 1 trip home per night of the dogsit: numNights(5.5(2*distance/25)
    print("hello")
    pricePerNight = data[cusID][2]/data[cusID][3]
    distance = data[cusID][6]
    totalGasPriceForStay = pricePerNight(5.5(2*(distance)/25))
    return ("Estimated total cost of gas is: $",totalGasPriceForStay)


def getQuarterlyEarnings():
    #using data, this will compute the total cost added together for each quarter based on dates
    dogsitRevenueCell= data[date][2]
    dogwalkRevenueCell = data[date][8]

    #TODO: create markers which can denote the quarter based on timestamp of hashtable
    #choose quarter: Q1, Q2, Q3, Q4
    #Q1
    for i in range(0, data[date]):
        if (dogsitRevenueCell != "nan"):
            dogsitRevenueQ1+= float(dogsitRevenueCell)
        elif (dogwalkRevenueCell != "nan"):
            dogwalkRevenueQ1+= float(dogwalkRevenueCell)
    #Q2
    for i in range(0, data[date]):
        if (dogsitRevenueCell != "nan"):
            dogsitRevenueQ2+= float(dogsitRevenueCell)
        elif (dogwalkRevenueCell != "nan"):
            dogwalkRevenueQ2+= float(dogwalkRevenueCell)
    #Q3
    for i in range(0, data[date]):
        if (dogsitRevenueCell != "nan"):
            dogsitRevenueQ3+= float(dogsitRevenueCell)
        elif (dogwalkRevenueCell != "nan"):
            dogwalkRevenueQ3+= float(dogwalkRevenueCell)
    #Q4
    for i in range(0, data[date]):
        if (dogsitRevenueCell != "nan"):
            dogsitRevenueQ4+= float(dogsitRevenueCell)
        elif (dogwalkRevenueCell != "nan"):
            dogwalkRevenueQ4+= float(dogwalkRevenueCell)
    totalQ1 = dogwalkRevenueQ1 + dogwalkRevenueQ1
    totalQ2 = dogwalkRevenueQ2 + dogwalkRevenueQ2
    totalQ3 = dogwalkRevenueQ3 + dogwalkRevenueQ3
    totalQ4 = dogwalkRevenueQ4 + dogwalkRevenueQ4

def TestDogsitPrice(numNights, numDogs, distance, numHolidays, numRate):
    #userprompt here 
    # select: numNights, numDogs, distance, numRate, etc.
    totalCost = numNights * (numDogs * numRate)

def TestPoop():
    cusIDBookings = {}
    bookingLineList = []
    for index in range(len(df.index)):
        name1 = df.loc[index, "Name"]  #get name 
        firstChar = name1[0] 
        secondChar = name1[1]
        intCode = (ord(firstChar) + ord(secondChar)) * 12 #hash function 
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
        cusIDBookings[intCode].extend(bookingLineList)
    print(bookingLineList)
    print(cusIDBookings)

