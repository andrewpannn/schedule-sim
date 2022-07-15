bigminute = 0

def runDay():
    minute = 1
    for x in range(20):
        runMinute(minute)
        minute += 1


def runMinute(minute):
    print(minute)

runDay()