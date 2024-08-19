import math

#Function provided by NEW: computes the avg of the numbers in the list grades
def calcAverage(grades):
    sum=0
    for aGrade in  grades:
        sum=sum + float(aGrade)
    average = sum / len(grades)
    roundedAvg = round(average)
    return roundedAvg

###Create list of values to test (invalid and valid)
test1=[0,0,0,0,0]
test2=["a","ten",5,"seven"]
test3=[90,75,88,85]
test4=[-10,-90,-55,-80]
test5=[]
test6=[" ", " "," ", " "]

# calcAverage(test2)

try:
    for num in test4:
        if num < 0:
            raise TypeError("Only integers are allowed")
    print(calcAverage(test4))
except ValueError:
    print("Type is not correct. Please provide a list of numbers.")
except ZeroDivisionError:
    print("List is empty. Please provide numbers.")
except Exception as e:
    print(e)

# try:
#     calcAverage(test2)
# except:
#     print('Input cannot be a string')



