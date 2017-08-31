import csv 
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta

csvfile = open("data/sleep-export.csv")
csvreader = csv.reader(csvfile, delimiter=',')
hours = []
#print type(csvreader)
for row in csvreader:
	if row[5] != "Hours":
		hours.append(row[5])

hours = np.array(hours)
hours.flags.writeable = True
validhours = []

# generate dates
days = []
start = date(2016, 9, 25)
end = date(2017, 8, 25)
delta = end - start

for j in range(delta.days + 1):
	days.append(start + timedelta(days=j))
	#print start + timedelta(days=j)

for i in range(0, len(days)):
	try:
		number = float(hours[i])
		if number < 1:
			number = 6.00
		validhours.append(number)
	except ValueError:
		validhours.append(7.50)
		#print "oh no! index ", i, " is invalid"
		#print "index ", i, " is: ", hours[i]
	

#print "two array lengths :", len(hours), len(validhours) 

# generate a mean value for the sleep hours for
# each interval 
interval = 7
chunks = []
meanhours = []
def divide(m, n):
	for i in range(0, len(m), n):
		yield m[i:i + n]

chunks = divide(validhours, interval)

for chunk in chunks:
	avg = np.mean(chunk)
	meanhours.append(avg)
	# for k in range(0, len(chunk)):
	# 	meanhours.append(avg)

#print meanhours, len(meanhours)
# generate weeks for the X axis
weeks = []
counter = 0
for val in meanhours:
	weeks.append(days[counter])
	counter += 7

print weeks, len(weeks)
print meanhours, len(meanhours)
meanhours = np.flipud(np.array(meanhours))
validhours = np.flipud(np.array(validhours))

# plot both
# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot(days, validhours)
# ax2.plot(weeks, meanhours)
# ax1.set_ylabel('hours sleep')
# ax1.set_xlabel('days')
# ax2.set_xlabel('weeks')

# plot mean only
plt.plot(weeks, meanhours)
plt.xlabel("Weeks")
plt.ylabel("Mean Hours Slept")
plt.tight_layout()
plt.show()