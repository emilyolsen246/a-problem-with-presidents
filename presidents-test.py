
from os import stat
import time
import csv
import statistics

class President:
    lived_years = 0
    lived_months = 0
    lived_days = 0
    dead = True
    def __init__(self, name, DoB, DoD):
        self.name = name
        self.DoB = DoB
        self.DoD = DoD
        if DoD == "":
            self.dead = False
    def getBirthYear(self):
        splittedDOB = self.DoB.split(", ")
        birthYear = splittedDOB[1]
        return birthYear
    def getDeathYear(self):
        if self.dead == False:
            return todaysYear
        else:
            splittedDOD = self.DoD.split(", ")
            dead = True
            deathYear = splittedDOD[1]
            return deathYear
    def getBirthMonth(self):
        splittedDOB = self.DoB.split(", ")
        firstHalf = splittedDOB[0]
        splittedfirstHalf = firstHalf.split(" ")
        birthMonth = splittedfirstHalf[0]
        return birthMonth
    def getDeathMonth(self):
        splittedDOD = self.DoD.split(", ")
        firstHalf = splittedDOD[0]
        splittedfirstHalf = firstHalf.split(" ")
        deathMonth = splittedfirstHalf[0]
        if deathMonth == "":
            dead = False
            return todaysMonth
        dead = True
        return deathMonth
    def getBirthDay(self):
        splittedDOB = self.DoB.split(", ")
        firstHalf = splittedDOB[0]
        splittedfirstHalf = firstHalf.split(" ")
        birthDay = splittedfirstHalf[1]
        return birthDay
    def getDeathDay(self):
        splittedDOD = self.DoD.split(", ")
        firstHalf = splittedDOD[0]
        splittedfirstHalf = firstHalf.split(" ")
        deathDay = splittedfirstHalf[1]
        if deathDay == "":
            dead = False
            return todaysDay
        dead = True
        return deathDay
    def setLivedYears(self, livedYears):
        self.lived_years = livedYears
    def setLivedMonths(self, livedMonths):
        self.lived_months = livedMonths
    def setLivedDays(self, livedDays):
        self.lived_days = livedDays
    def getLivedYears(self):
        return self.lived_years
    def getLivedMonths(self):
        return self.lived_months
    def getLivedDays(self):
        return self.lived_days
    def isHeDead(self):
        return self.dead


class Month:
    def __init__(self, name, number, numOfDays):
        self.name = name
        self.number = number
        self.numOfDays = numOfDays
    def getName(self):
        return self.name
    def getNumber(self):
        return self.number
    def getNumOfDays(self):
        return self.numOfDays


def yearsToDays(years):
    return (years * 365)


months = []
January = Month("Jan", 1, 31)
months.append(January)
February = Month("Feb", 2, 28)
months.append(February)
March = Month("Mar", 3, 31)
months.append(March)
April = Month("Apr", 4, 30)
months.append(April)
May = Month("May", 5, 31)
months.append(May)
June = Month("Jun", 6, 30)
months.append(June)
July = Month("Jul", 7, 31)
months.append(July)
August = Month("Aug", 8, 31)
months.append(August)
September = Month("Sep", 9, 30)
months.append(September)
October = Month("Oct", 10, 31)
months.append(October)
November = Month("Nov", 11, 30)
months.append(November)
December = Month("Dec", 12, 31)
months.append(December)


def monthsToDays(startMonth, endMonth):
    totalDays = 0
    x = startMonth
    while x < endMonth:
        totalDays = totalDays + months[x].numOfDays
        x = x + 1
    return totalDays


presidentList = []
birthMonth = 0
deathMonth = 0


with open('U.S. Presidents Birth and Death Information - Sheet1.csv') as csvFile:
    csvReader = csv.reader(csvFile)
    lineNum = 1
    for row in csvReader:
        if lineNum > 0 and lineNum < 46:
            presidentList.append(President(row[0], row[1], row[3]))


from datetime import date
fullToday = str(date.today())
todaySplit = fullToday.split("-")
todaysYear = int(todaySplit[0])
todaysMonth = int(todaySplit[1])
todaysDay = int(todaySplit[2])


i = 1
while i < (len(presidentList) - 1):
    # setting years lived
    birthYear = int(presidentList[i].getBirthYear())
    deathYear = int(presidentList[i].getDeathYear())
    presidentList[i].setLivedYears(deathYear - birthYear)
    
    # setting months lived
    j = 0
    while j < len(months):
        if presidentList[i].getBirthMonth() == months[j].name:
            birthMonth = months[j].getNumber()
        j = j + 1
    k = 0
    while k < len(months):
        if presidentList[i].getDeathMonth() == months[k].name:
            deathMonth = months[k].number
        k = k + 1
    livedYears = presidentList[i].getLivedYears()
    presidentList[i].setLivedMonths((deathMonth - birthMonth) + (livedYears * 12))

    # setting days lived
    livedYearsToDays = yearsToDays(presidentList[i].getLivedYears())
    livedMonthsToDays = monthsToDays(birthMonth, deathMonth)
    livedDays = livedYearsToDays + livedMonthsToDays
    x = 0
    while x < len(months):
        if birthMonth == months[x].number:
            livedDays = livedDays + (months[x].numOfDays - int(presidentList[i].getBirthDay()))
        x = x + 1
    presidentList[i].setLivedDays(livedDays)
    i = i + 1


# Printing longest living top 10
highToLow = sorted(presidentList, key=lambda president: president.lived_days, reverse=True)
print("\n")
print("Top 10 Longest Living Presidents:")
print("--------------------------------------------")
y = 0
while y < 10:
    if highToLow[y].isHeDead() == False:
        print(str(y + 1) + ". " + highToLow[y].name + " has lived " + str(highToLow[y].getLivedDays()) + " days so far!")
    else:
        print(str(y + 1) + ". " + highToLow[y].name + " lived " + str(highToLow[y].getLivedDays()) + " days!")
    print("--------------------------------------------")
    y = y + 1


print("\n")
# Printing shortest living top 10
lowToHigh = sorted(presidentList, key=lambda president: president.lived_days, reverse=False)
print("Top 10 Shortest Living Presidents:")
print("--------------------------------------------")
z = 2
while z < 12:
    if lowToHigh[z].isHeDead() == False:
        print(str(z - 1) + ". " + lowToHigh[z].name + " has lived " + str(lowToHigh[z].getLivedDays()) + " days so far!")
    else:
        print(str(z - 1) + ". " + lowToHigh[z].name + " lived " + str(lowToHigh[z].getLivedDays()) + " days!")
    print("--------------------------------------------")
    z = z + 1



presLivedDaysList = []
j = 1
while j < (len(presidentList) - 1):
    presLivedDaysList.append(presidentList[j].getLivedDays())
    j = j + 1


# mean, weighted mean, median, mode, max, min, standard deviation (round to 2 dec)
tempweightedMean = statistics.harmonic_mean(presLivedDaysList)
weightedMean = round(tempweightedMean, 2)
median = statistics.median(presLivedDaysList)
mode = statistics.mode(presLivedDaysList)
tempmean = statistics.mean(presLivedDaysList)
mean = round(tempmean, 2)
maximum = max(presLivedDaysList)
minimum = min(presLivedDaysList)
tempstandardDev = statistics.stdev(presLivedDaysList)
standardDev = round(tempstandardDev, 2)

print("\n")
print("Statistics of Lived Days:")
print("----------------------------------")
print("The mean is: " + str(mean))
print("----------------------------------")
print("The weighted mean is: " + str(weightedMean))
print("----------------------------------")
print("The median is: " + str(median))
print("----------------------------------")
print("The mode is: " + str(mode))
print("----------------------------------")
print("The max is: " + str(maximum))
print("----------------------------------")
print("The min is: " + str(minimum))
print("----------------------------------")
print("The standard deviation is: " + str(standardDev))
print("----------------------------------")
print("\n")