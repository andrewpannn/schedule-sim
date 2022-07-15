import random

washers = 6
population = 800
peopleIndex = []
startDay = 0  # 0 is monday, 6 is sunday
minute = 0  # minute 0 is 00:01


class Person:
    def __init__(self, dirtyClothes, schedule, free):
        self.totalClothes = 7 + random.randint(0, 6)
        self.dirtyClothes = dirtyClothes
        self.tower = random.randint(0, 1)  # North is 0 South is 1
        self.schedule = schedule
        self.free = free
        self.credits = random.randint(12,18)



def runMinute(minute, free):
    for person in peopleIndex:
        if free == 1:
            run

    minute += 1

def runDay():
    while minute < 1440:
        runMinute(minute)

def generatePeople():
    for x in range(population):
        peopleIndex.append(Person(random.randint(0, 6)))

def generateWeekday():
    for person in peopleIndex:
        hours = person.credits
        twoHour = 2*random.randint(0,2)
        oneHour = hours - twoHour
        


def generateSchedule():
    for person in peopleIndex:
        person.schedule = [[],[],[],[],[],[],[]]

