"""
Refactor the PersonTester program from course 1 to:
-Create menu to allow user to:
---modify persons name
---change date and time avail
---print report of all and teir abail
---remove person from team

"""
"""
----------------Notes---------------
-Can use bool variable and make menu with if and elifs

"""
import smtplib, ssl
import tkinter
#import tinker.filedialog import askopenfile
import csv
#################################Course 1 Portfolio Project#################################

##Create Person class with first name, last name, available days
##, and available times as lists

#Person Object from Week 4
class Person:
    def __init__(self,firstName,lastName,dateOne,dateTwo,timeOne,timeTwo):
        self.firstName=firstName
        self.lastName=lastName
        self.dateOne=dateOne
        self.dateTwo=dateTwo
        self.timeOne=timeOne
        self.timeTwo=timeTwo
    #display the name, and possible date/times
    def display(self):
        return [self.firstName,self.lastName,self.dateOne,self.dateTwo,self.timeOne,self.timeTwo]

#function for time conversion from Week 3
def findStandardTime(militaryTime):
    #For 1pm-9:59pm
    if int(militaryTime) >= 1300 and int(militaryTime) < 2200:
        timeOfDay="pm"
        newTime=int(militaryTime) - 1200
        newTime = "0" + str(newTime)
    #For 10:00pm +
    if int(militaryTime) >= 2200:
        timeOfDay="pm"
        newTime=int(militaryTime) - 1200
        newTime = str(newTime)
    #For 12pm-12:59pm
    elif int(militaryTime) >= 1200 and int(militaryTime) < 1300:
        timeOfDay="pm"
        newTime=str(militaryTime)
    #For 12:01am-11:59am
    elif int(militaryTime) < 1200:
        timeOfDay="am"
        newTime=str(militaryTime)
    hour=newTime[:2]
    minutes = newTime[2:]
    return hour + ":" + minutes + timeOfDay

#Will hold the Person objects - this list used for listing teammates
allPersons = []
#Holds person objects - this list used for storing Person as list object
personObjList=[]

def createNewPerson():
    print("Please provide the following information:")
    #from while loop from Week 4
    input1=input("Enter your first name:")
    input2=input("Enter your last name:")
    input3=input("Enter your first available date in the following format MM/DD:")
    input4=input("Enter your second available date in the following format MM/DD:")
    #convert inputs 5 and 6 to standard time
    input5=findStandardTime(input("Enter your first available time:"))
    input6=findStandardTime(input("Enter your second available time:"))
    #creates new person based on the inputs
    newPerson = Person(input1,input2,input3,input4,input5,input6)
    #allPersons.append(newPerson.display())
    #team.append(newPerson.display())
    return newPerson


def addToTeam(person):
    allPersons.append(Person(person.firstName,person.lastName,person.dateOne,person.dateTwo,person.timeOne,person.timeTwo))
    #allPersons.append(person)
    #for the print all option 
    personObjList.append(person.display())
    return True

#Adding sample team members 
example=Person("Steven","Universe","07/01","06/03",findStandardTime(1400),findStandardTime(1100))
example2=Person("Greg","Universe","06/01","07/01",findStandardTime(1100),findStandardTime(1330))
example3=Person("Harry","Potter","06/03","07/01",findStandardTime(1100),findStandardTime(1340))

addToTeam(example)
addToTeam(example2)
addToTeam(example3)

#Importing Tabulate to help present the data as a table
from tabulate import tabulate

def printAll(team):
#Creating the header titles for the table
    header = ["First Name","Last Name","1st Available Date","2nd Available Date","1st Available Time","2nd Available Time"]
#Display the table
    return tabulate(team,headers=header,tablefmt="grid")

def findPerson(name):
    found=Person
    for person in allPersons:
        #if name == (person.firstName + " " + person.lastName):
        fullName=(person.firstName + " " + person.lastName)
       # print(fullName)
        if name in fullName:
            found=person
            break
        #else:
            #return print("Sorry, {} couldn't be founD".format(name))
    #should be a Person object
    return found

#brings in Person object, use findPerson first
def updateName(person):
    #foundPerson=findPerson(person)
    if person in allPersons:  
        #print(foundPerson)
        originalFirst=person.firstName
        originalLast=person.lastName

        print("Enter new first name:")
        newFirstName=input()
        person.firstName = newFirstName
        print("Enter new last name:")
        newLastName=input()
        person.lastName = newLastName
        print("{} has been updated".format(person.display()))
    else:
      return print(("Sorry, {} could not be found. Please try again").format(person))
  
    for item in personObjList:
        #if item.contains(person.firstName and person.lastName):
        if originalFirst in item and originalLast in item:
            personObjList.append(person.display())
            personObjList.remove(item)
    return True

def updateTimeDate(person):
    #foundPerson=findPerson(person)
    if person in allPersons:  
        #print(foundPerson)
        originalFirst=person.firstName
        originalLast=person.lastName

        print("Enter new first available date:")
        newFirstDate=input()
        person.dateOne = newFirstDate
        print("Enter new second available date:")
        newSecDate=input()
        person.dateTwo = newSecDate
        print("Enter new first available time:")
        newFirstTime=input()
        person.timeOne = newFirstTime
        print("Enter new second available time:")
        newSecTime=input()
        person.timeTwo = newSecTime
        print("{} has been updated".format(person.display()))
    else:
      return print(("Sorry, {} could not be found. Please try again").format(person))
  
    for item in personObjList:
        #if item.contains(person.firstName and person.lastName):
        if originalFirst in item and originalLast in item:
            personObjList.append(person.display())
            personObjList.remove(item)
    return True    

def RemoveMember(person):
    if person in allPersons:  
        #print(foundPerson)
        originalFirst=person.firstName
        originalLast=person.lastName
        allPersons.remove(person)
    for item in personObjList:
        #if item.contains(person.firstName and person.lastName):
        if originalFirst in item and originalLast in item:
            personObjList.remove(item)
    return True 

def emailSchedule():
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "emberschumpna@gmail.com"
    receiver_email = "emberschumpna@gmail.com"
    password = "tsoe otqb olew mpqt"
    message = printAll(personObjList)

    context = ssl.create_default_context()
    print("hi")
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        print("hi")
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
#################################Course 2 Portfolio Project#################################

#################################Course 3 Week 4#################################
##Create menu item that will prompt user for name of the path/csv file, func that will take the file (read) create a list of objects with all team member info
def getFile():
    #file = askopenfile(mode='r',filetypes=[csvFile, '.csv'])
    print("Enter file name:")
    filename=input()
    # results=[]
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            # results.append(row)
            personObjList.append(row)
    # allPersons.append(Person(person.firstName,person.lastName,person.dateOne,person.dateTwo,person.timeOne,person.timeTwo))

            person=(Person(row[0],row[1],row[2],row[3],row[4],row[5]))
            allPersons.append(person)
    print(personObjList)

#Add menu item to allow user to write all data in the list of objects to a csv file
##prompt user for file name

def saveAll():
    filename=input("Provide a file name:")
    with open(filename,mode='w',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(personObjList)

###############################Helper Methods################
#####Compare the times and days for each person and return common time

#Pull list of team
#Iterate through list to view/compare times for each person
#return time with the most common occurrence
#if no time matches, return message
#will pass in allPerson list (Person objects)
def commonTime(list):
    count=0
    potentialDates=[]
    #each person in allPerson
    for item in list:
        matchOne= item.dateOne + " " + str(item.timeOne)
        matchTwo= item.dateOne + " " + str(item.timeTwo)
        matchThree= item.dateTwo + " " + str(item.timeOne)
        matchFour= item.dateTwo + " " + str(item.timeTwo)

        personDates = [matchOne, matchTwo, matchThree, matchFour]
        #adds the date/time pairs for each person as its own list object within potentialDates
        potentialDates.append(personDates)

    #iterate through potential dates
    #compare item to the 
    common_values=set(potentialDates[0])
    for times in potentialDates[1:]:
        common_values &= set(times)
    return common_values
    ###Action: Add something for when there's no common values
        
            
####Display full report plus the common available meeting time
###Use the common time helper method and display report that includes common time
##maybe print the common time after the table?
menu=True

print("1 Add new team member\n"
      + "2 Print full schedule\n"
      + "3 Update Team Member Name\n"
      + "4 Update Availability\n"
      + "5 Find person\n"
      + "6 Remove Team Member\n"
      + "7 Send Schedule as Email\n"
      + "8 Open file\n"
      + "9 Save Team List\n"
      + "10 Check Availability\n"
      + "11 Exit Program\n"
      + "12 Test Cases")
option=input()

while menu:
    if option=="1":
        action=createNewPerson()
        addToTeam(action)
        print("{} has been added to the team.".format(action.firstName))
        #print(allPersons)
    elif option=="2":
        print(printAll(personObjList))
        times=commonTime(allPersons)
        if times==set():
            print("\nSorry, there are no common appointment times for this group. Please request new availability.")
        else:
            print("Your team members have a matching availability of {}".format(times))
        input("Enter any key to return to menu...")
    elif option=="3":
        print("Please enter which name you'd like to update:")
        name=input()
        foundPerson=findPerson(name)
        print(foundPerson.display())
        updateName(foundPerson)
    elif option=="4":
        #print(allPersons)
        print("To update availability, please enter the name of the team member:")
        name=input()
        foundPerson=findPerson(name)
        print(foundPerson.display())
        updateTimeDate(foundPerson)
    elif option=="5":
        print("Please enter the first or last name of the team member you'd like to find:")
        name=input()
        requestedPerson=findPerson(name)
        print(requestedPerson.display())
    elif option=="6":
        print("Please enter the name of the team member you'd like to remove:")
        name=input()
        foundPerson=findPerson(name)
        RemoveMember(foundPerson)
    elif option=="7":
        emailSchedule()
    elif option=="8":
        getFile()
    elif option=="9":
        saveAll()
        exit()
    elif option=="10":
        times=commonTime(allPersons)
        if times==set():
            print("Sorry, there are no common appointment times for this group. Please request new availability.")
        else:
            print("Your team members have a matching availability of {}".format(times))
        input("any key..")
    elif option=="11":
        print("Thanks for using our service. Have a great day!")
        input("Enter any key to exit...")
        exit()
    elif option=="12":
        test1="ewrefsd"
        testcase2=Person("test","test","06/01","07/01",findStandardTime("1400"),findStandardTime(1300))
        try:
            findStandardTime(test1)
        except ValueError:
            print("The string provided to int could not be parsed as an integer")
        except Exception as e:
            print(e)
        input("Enter any key to exit...")

    print("Select new option:")
    print("1 Add new team member\n"
      + "2 Print full schedule\n"
      + "3 Update Team Member Name\n"
      + "4 Update Availability\n"
      + "5 Find person\n"
      + "6 Remove Team Member\n"
      + "7 Send Schedule as Email\n"
      + "8 Open file\n"
      + "9 Save Team List\n"
      + "10 Check Availability\n"
      + "11 Exit Program\n"
      + "12 Test Cases")
    option=input()
    if option=="n":
        break

#     ####################Test Cases#########################
# #string for time instead of int
# test1="werywre"
# testcase2=Person("test","test","June 1st","July 1st","1400",1300)
# try:
#     findStandardTime(test1)
# except Exception as e:
#     print(e)
