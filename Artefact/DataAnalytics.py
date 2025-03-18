import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import numbers
import matplotlib.pyplot as plt
import numpy as np
cred = credentials.Certificate("computersciencediddly-firebase-adminsdk-apdja-ed7c3b9cd8.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://computersciencediddly-default-rtdb.europe-west1.firebasedatabase.app'})
ref = db.reference('/')

catalogue = ref.get()

masses = []
classes = []
classTypes = []
classTypes_dict = {}

classesInt = []
birthdays = []
names = []
heft_dict = {}

# grabbing names ↓

for i in range(len(catalogue['name'])):
    name = catalogue['name'][i]
    names.append(name)
    
# hefty chart ↓

for i in range(len(catalogue['mass (g)'])):
    mass = catalogue['mass (g)'][i]
    masses.append(mass)

print(masses)

print("\nFinding lightest specimen...")

lightest = 1000
for weight in masses:
    if weight < 0.01:
        print("no!")
    else:
        if weight < lightest:
            lightest = weight
        else:
            pass

print(str(lightest) + " grams")
mgLightest = lightest * 1000
mgLightest = int(mgLightest)
print(str(mgLightest) + " milligrams.")

print("\nFinding heftiest specimen...")

heaviest = 0
for heft in masses:
    if heft > heaviest:
        heaviest = heft
    else:
        pass
heaviest = int(heaviest)

print(str(heaviest) + " grams")
hKilos = heaviest / 1000
hKilos = int(hKilos)
print(str(hKilos) + " kilograms")
hTonnes = hKilos / 1000
hTonnes = int(hTonnes)
print(str(hTonnes) + " metric tonnes\n")

sortedWeights = sorted(masses)

print(sortedWeights)

heftLabels = (heft_dict.keys())
heftKeys = (heft_dict.values())

heaviestMrk = 850
Interval = 1000
mrk1 = 0
mrk2 = 1000
amount = 0

massGroups = []
massCounts = []
heft_dict = {}

while mrk2 < 4000001:
    Amount = 0
    mrk1 = mrk1 + Interval
    mrk2 = mrk2 + Interval
    for i in sortedWeights:
        if i >= mrk1 and i <= mrk2:
            Amount = Amount + 1
        else:
            pass
    if Amount == 0:
        pass
    elif Amount > 0:
        massGroups.append(str(mrk2))
        massCounts.append(Amount)
        print("There are " + str(Amount) + " meteors that weigh between the masses " + str(mrk1) + " and " + str(mrk2) + " grams.")

plt.plot(massGroups, massCounts)  # Plot the chart
plt.show()

for i in massGroups:
    Indexed = massGroups.index(i)
    heft_dict[i] = massCounts[Indexed]
print(heft_dict)

# type seperation pie chart yoke ↓
 
for i in range(len(catalogue['class'])):
    metClass = catalogue['class'][i]
    classes.append(metClass)

sortedClasses = sorted(classes)
for i in sortedClasses:
    if i[0] == "H":
        i = i[0:2]
    elif i[0:2] == "LL":
        i = i[0:3]
    elif i[0] == "L" and i[1].isdigit() == True:
        i = i[0:2]

    if i in classTypes:
        pass
    else:
        classTypes.append(i)

print(classTypes)

for i in classTypes:
    classTypes_dict[i] = sortedClasses.count(i)
    classesInt.append(sortedClasses.count(i))

print(classTypes_dict)

pieLabels = list(classTypes_dict.keys())
pieKeys = list(classTypes_dict.values())

plt.pie(pieKeys, labels=pieLabels)
plt.show()

# birthday chart ↓

for i in range(len(catalogue['year'])):
    year = catalogue['year'][i]
    year = int(year)
    birthdays.append(year)
birthdays = sorted(birthdays)

oldest = 850
interval = 10
marker1 = 1740
marker2 = 1750
amount = 0

print("\nAccording to the dataset...\n")

yearGroups = []
yearCounts = []
birthdays_dict = {}

while marker2 < 2020:
    amount = 0
    marker1 = marker1 + interval
    marker2 = marker2 + interval
    yearGroups.append(str(marker2))
    for i in birthdays:
        if i >= marker1 and i <= marker2:
            amount = amount + 1
        else:
            pass
    yearCounts.append(amount)
    print("There are " + str(amount) + " meteors that landed between the years " + str(marker1) + " and " + str(marker2) + ".")

plt.plot(yearGroups, yearCounts)  # Plot the chart
plt.show()

print(yearGroups)
print(yearCounts)

for i in yearGroups:
    indexed = yearGroups.index(i)
    birthdays_dict[i] = yearCounts[indexed]
print(birthdays_dict)
    

