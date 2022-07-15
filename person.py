import numpy as np
import random

np.set_printoptions(threshold=np.inf)

hourLength = 60
halfHour = 0
southWashers = 7
northWashers = 7

# this set represents the possible hour-hour interval a class can be held
classAvail = set()
for x in range(16, 39):
    classAvail.add(x)


# defines the variable in the person object. Each person in Haggett is an object
class Person:
    def __init__(self):
        self.credits = random.randint(12, 18)  # random number of credits
        self.schedule = np.zeros((7, 1440), dtype=int)  # this will store an array representing when they are free
        self.totalClothes = random.randint(7, 10)
        self.dirtyClothes = random.randint(0, 6)
        self.cleanClothes = self.totalClothes - self.dirtyClothes
        self.free = False
        self.tower = random.randint(0, 1)  # 0 is south, 1 is north
        self.urgency = 0  # a value from 0 to 1. 1 is maximum urgency
        self.bedTime = 0
        self.wakeTime = 0
        self.urgencyMinLeft = 0


testIndex = [Person()]  # creates one object


# just resets the classAvail set each day
def resetClassAvail():
    classAvail.clear()
    for x in range(16, 39):
        classAvail.add(x)


# changes the person's schedule by making any "busy" minutes into a 1
def applyClass(dayNum, thisHour, hourLengthApply):
    minuteLength = hourLengthApply
    minuteStart = thisHour
    minuteEnd = minuteStart + 2 * minuteLength
    print(minuteLength, minuteStart, minuteEnd)
    for y in range(minuteStart * 30, minuteEnd * 30):
        person.schedule[dayNum, y] = 1


# creates a sleep schedule, then modifies the person.schedule array
def generateSleepSchedule():
    sleepStartTime = random.randint(1320, 1560) % 1440
    sleepAmount = random.randint(360, 540)
    sleepEndTime = (sleepStartTime + sleepAmount) % 1440
    person.bedTime = sleepStartTime
    person.wakeTime = sleepEndTime
    for y in range(0, 6):
        if sleepStartTime < 1320:  # this is if the sleep time is AFTER midnight
            for x in range(sleepStartTime, sleepEndTime):
                person.schedule[y, x] = 1
        else:  # this is if the sleep time is BEFORE midnight, so it will fill up the current day and the next day
            for x in range(sleepStartTime, 1440):
                person.schedule[y, x] = 1
            for x in range(0, sleepEndTime):
                person.schedule[y, x] = 1


# each time this is run, it will create a hour class and add it to the person's schedule. Then it deletes the time
# sections from the class availability
def generateClass(hourLengthGenClass, dayNum):
    while True:  # infinite loop
        thisHour = random.sample(classAvail, k=1)
        thisHourInt = thisHour[0]
        if {thisHourInt + i for i in range(2 * hourLengthGenClass)}.issubset(
                classAvail):  # checks whether the spots are
            # available in the overall schedule. If it's a one-hour class, there can't be another class half an hour
            # after "thisHour". Similarly, with two-hour, there must be 3 open slots in front of it.
            for x in range(2 * hourLengthGenClass):
                classAvail.discard(thisHourInt + x)  # removes the time segments from the classAvail set
            break
    applyClass(dayNum, thisHourInt, hourLengthGenClass)
    print(thisHour, hourLengthGenClass)


# creates class schedule for each day. Takes in the number of credits the person has, and which day it's affecting
def generateDay(credits, dayNum):
    twoHourNum = 0
    resetClassAvail()
    if credits > 1:
        twoHourNum = random.randint(0, 1)  # this is generating the number of one-hour and two-hour classes
        if credits > 4:
            twoHourNum = random.randint(1, 2)
    oneHourNum = credits - 2 * twoHourNum
    for x in range(oneHourNum):
        generateClass(1, dayNum)
    for x in range(twoHourNum):
        generateClass(2, dayNum)


# randomly creates a class schedule, then fills in 1s in person.schedule for unavailable times
def generateClassSchedule():
    creditsNum = person.credits
    m_w_f = random.randint(3, 4)
    t = random.randint(0, creditsNum - 3 * m_w_f)
    if t > 5:
        t = t - 3
    th = creditsNum - 3 * m_w_f - t
    print(m_w_f, "mwf")
    print(t, "t")
    print(th, "th")
    print("Monday")
    generateDay(m_w_f, 1)
    print("Tuesday")
    generateDay(t, 2)
    print("Wednesday")
    generateDay(m_w_f, 3)
    print("Thursday")
    generateDay(th, 4)
    print("Friday")
    generateDay(m_w_f, 5)
    print("how many credits: ", creditsNum)


# if the person has time to do laundry, their "free" will be True
def isFree(dayNum, minuteNum):
    whichDay = dayNum
    nextDayRange = 0
    topRange = 1440 - minuteNum
    if topRange >= 90:
        topRange = 90
    else:
        nextDayRange = 90 - topRange
    for z in range(minuteNum, minuteNum + topRange):  # the topRange variable exists so that it doesn't check beyond
        # the limit of the array
        if person.schedule[whichDay, z] == 1:
            person.free = False
            break
        else:
            person.free = True
    if nextDayRange > 0:  # If the minNum is more than 1350, then this checks the availability of the next day
        if dayNum == 6:
            whichDay = 0
        else:
            whichDay = dayNum + 1
        for z in range(0, nextDayRange):
            if person.schedule[whichDay, z] == 1:
                person.free = False
                break
            else:
                person.free = True


def runDay(dayNum):
    minute = 0
    person.dirtyClothes += 1
    person.cleanClothes = person.totalClothes - person.dirtyClothes
    for x in range(1440):
        runMinute(dayNum, minute)
        minute += 1


# determines how badly a person needs to do laundry
def determineUrgency(urgMin):
    if urgMin == person.wakeTime:
        monkey = 0
    minLeft = (person.bedTime - urgMin)



# performs the actions that occur every minute
def runMinute(dayNum, min):
    isFree(dayNum, min)


for person in testIndex:
    generateClassSchedule()
    generateSleepSchedule()
    runDay(0)
    runDay(1)
    runDay(2)
    runDay(3)
    runDay(4)
    runDay(5)
    runDay(6)

