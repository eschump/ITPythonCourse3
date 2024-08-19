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

input=findStandardTime(input("Please enter time:"))
print(input)