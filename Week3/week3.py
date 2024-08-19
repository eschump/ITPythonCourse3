import re

##Check if a string has certain set of char 

examplestr = "woR5ds23_"
searchedResult=re.search("^[a-zA-Z0-9_]+$",examplestr)
print(searchedResult)

#^ starts
#$ ends

##write program to find sequences of lowercase letters joined with an underscore
example2="aa_bb_ccb"
newResult=re.search(r"\b([a-z]{2}_)+[a-z]{2}\b",example2)
print(newResult)

##Write a program to remove leading zeros from an IP address 
example3="192.001.001.001"
third=re.search(r"\b0+(?=[0-9])",example3)
print(third)

def remove_leading_zeros(ip):
    pattern = re.compile(r'\b0+(?=[0-9])')
    return pattern.sub('', ip)

print(remove_leading_zeros(example3))