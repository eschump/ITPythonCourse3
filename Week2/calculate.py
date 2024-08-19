#Week 2: Create 2 programs to do the following:
# second program (calulate.py) goes through each row and calculates the average to the 5 numbers in each row.
import csv

with open('practicefile.csv',mode='r')as file:
    csvFile = csv.reader(file)
    #display content
    for row in csvFile:
        numbers=row.split(',')
        # out=[(numbers[i:i+] )] [0,len(numbers),2]
