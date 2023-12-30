# Python Program for Dog Sitting Business Bookkeeping

## Overview
This Python program utilizes the Pandas library to manage a bookkeeping sheet for a dog sitting business. It includes functionality to track, update, and view data within the sheet.

## Getting Started

### Prerequisites
- Python 3.x
- Pandas library
- NumPy library
- An Excel file (`DogsittingBook.xlsx`) containing the dog sitting business data

### Installation
1. Ensure Python 3.x is installed on your machine.
2. Install Pandas and NumPy libraries using pip:
```
pip install pandas numpy
```
3. Clone or download this repository to your local machine.
4. Place the `DogsittingBook.xlsx` file in the same directory as the script.

### Running the Program
Execute the script using Python:
```
python dog_sitting_bookkeeping.py
```

## Code Description

### `dog_sitting_bookkeeping.py`
- **Functionality**:
  - Reads data from an Excel file using Pandas.
  - Includes various functions to manipulate and query the data:
    - `getAllCusIDBookings()`: Retrieves all customer ID bookings.
    - `HashTable` class: Implements a hash table for efficient data storage and retrieval.
    - `getBookingsByID()`: Obtains bookings by customer ID.
    - `getBookingsByDate()`: Retrieves bookings by date.
    - `getGasData()`: Calculates estimated gas costs.
    - `convertDatetoDay()`: Converts a date string to a datetime object.
    - `getQuarterlyEarnings()`: Computes earnings for a specified quarter.
    - `TestDogsitPrice()`: Tests the dog sitting price calculation.

- **Challenges Faced**: 
  - Implementing custom hash functions for customer identification.
  - Efficiently handling data retrieval and manipulation.
  - Integrating Excel file operations with Python.

## Acknowledgments
- This project is inspired by the need for an efficient way to handle bookkeeping in a small dog sitting business.

## Author
Logan F
