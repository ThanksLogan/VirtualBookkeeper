#this is the file for my shii cuhhh
from pyxll import xl_func
import pandas as pd
import numpy as np
from collections import defaultdict
print("...program starting...                                       :)")
#Dee is the variable name of our workbook
#Dee = load_workbook('arg1')

df = pd.read_excel('C:\\project\\DogsittingBook.xlsx') 

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

def createCustomerIDList(HashTable):
    name_List = []
    for index in range(len(df.index)):
        name = df.loc[index, "Name"] #name of person
        name_List.append(name)
    #generate unique customer id for each line in namelist
    name_List.sort()
    temp = defaultdict(lambda: len(temp))
    idList = [temp[ele] for ele in name_List]
    for i in range(len(idList)):
        hash_table.set_val(idList[i], name_List[i])
    return HashTable

hash_table = HashTable(len(df.index))
cusIDs = createCustomerIDList(hash_table)
print(cusIDs)


