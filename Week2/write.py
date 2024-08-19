#Week 2: Create 2 programs to do the following:
# create a csv file with 5 rows of 5 random numbers between 50 and 100 separated by tabs.
import csv 
import random
#header names
# headers = ['Num1','Num2','Num3''Num4','Num5']

#data
# rows=[str(random.randint(50,100)), str(random.randint(50,100)), str(random.randint(50,100)), str(random.randint(50,100)), str(random.randint(50,100))]

f = open("list.csv", "w", newline='')
# number=random.randint(50,100)
# x=0
# while x<6:
#       f.write(str(random.randint(50,100)))
#       f.write("\n")
#       x+=1

# with open(f,'w', newline=''):
#     #creating csv writer object
x=0
while x<5:
      csvwriter = csv.writer(f)
      csvwriter.writerow([str(random.randint(50,100)), str(random.randint(50,100)), str(random.randint(50,100)), str(random.randint(50,100)), str(random.randint(50,100))])
      x+=1


