import pandas as pd


df = pd.ExcelFile("/Users/loganforeman/Desktop/Python prod/DogsittingBook.xlsx")
data=df.parse("DogsittingBook.xlsx")
print(data.head(10))