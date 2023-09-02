def extractWeatherData(json):
    
    element = json['records']['location'][0]['weatherElement']

    wx = []
    pop = []
    mint = []
    maxt = []

    for i in range(len(element)):
        if i == 0:
            wx.append(element[0])
        elif i == 1:
            pop.append(element[1])
        elif i == 2:
            mint.append(element[2])
        elif i == 3:
            maxt.append(element[3])

    return wx, pop, mint, maxt

def splitWeatherData(json):
    weatherElementLen = len(json)

    weatherslotLen = len(json[0][0]['time'])

    wx = []
    pop = []
    mint = []
    maxt = []

    for i in range(weatherElementLen):
        for j in range(weatherslotLen):
            if i == 0:
                wx.append(json[i][0]['time'][j]['parameter']['parameterName'])
            elif i == 1:
                pop.append(json[i][0]['time'][j]['parameter']['parameterName'])
            elif i == 2:
                mint.append(json[i][0]['time'][j]['parameter']['parameterName'])
            elif i == 3:
                maxt.append(json[i][0]['time'][j]['parameter']['parameterName'])
    
    return wx, pop, mint, maxt
            
def extractWeatherTime(json):
    time = json['records']['location'][0]['weatherElement'][0]['time']

    startTime = []
    endTime = []

    for i in range(len(time)):
        startTime.append(time[i]['startTime'])
        endTime.append(time[i]['endTime'])  
    
    return startTime, endTime

def splitWeatherTime(json):
    timePeriod = []
    for i in range(3):
        startTimeSplit = json[0][i].split(' ')
        startTimeDate = startTimeSplit[0].split('-')[1] + '/' + startTimeSplit[0].split('-')[2]
        startTimePeriod = startTimeSplit[1].split(':')[0] + ':' + startTimeSplit[1].split(':')[1]
        startTime = startTimeDate + ' ' + startTimePeriod

        endTimeSplit = json[1][i].split(' ')
        endTimeDate = endTimeSplit[0].split('-')[1] + '/' + endTimeSplit[0].split('-')[2]
        endTimePeriod = endTimeSplit[1].split(':')[0] + ':' + endTimeSplit[1].split(':')[1]
        endTime = endTimeDate + ' ' + endTimePeriod  

        timePeriod.append(startTime + ' - ' + endTime)

    return timePeriod
