import csv
import datetime

with open('attendance.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    now = datetime.datetime.now()
    writer.writerow(['{} people swiped in for event on {}'.format(5, now.strftime("%m/%d/%Y")) ])