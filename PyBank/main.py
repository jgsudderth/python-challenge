#standard code to load a csv

import csv
import os

# define file path
csv_path = os.path.join("..", "Resources", "budget_data.csv")

#create empty lists for months and revenue
months = []
revenue = []

#import data file into python
with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    
    #skip header row
    next(reader, None)
    #iterate over rows and append unique months and their respective revenue to their lists
    for row in reader:
        months.append(row[0])
        revenue.append(int(row[1]))

#determine the total months and store as a variable
total_months = len(months)

#set intial values for greatest increase, decrease, and total revenue (should all be 0 or the first value)
max_increase = revenue[0]
max_decrease = revenue[0]
total_revenue = 0

#iterate over rows and determine if the change in revenue is higher than any day before it... if so than 
#set the variable to be the new value
#add each revenue value to the total revenue (+=)

for r in range(len(revenue)):
    if revenue[r] >= max_increase:
        max_increase = revenue[r]
        greatest_month_increase = months[r]
    elif revenue[r] <= max_decrease:
        max_decrease = revenue[r]
        greatest_decrease_month = months[r]
    total_revenue += revenue[r]

#find the average change over the entire data set (total revenue divided by total months)
average_change = round(total_revenue/total_months, 2)


#pring to text file
with open('Output.txt', 'w') as text_file:
    text_file.write('Financial Analysis' + '\n')
    text_file.write('----------------------------' + '\n')
    text_file.write('Total Months: ' + str(total_months) + '\n')
    text_file.write('Total Revenue: $' + str(total_revenue) + '\n')
    text_file.write('Greatest Increase in Revenue: ' + greatest_month_increase + ' ($' + str(max_increase) + ')'+ '\n')
    text_file.write('Greatest Decrease in Revenue: ' + greatest_decrease_month + ' ($' + str(max_decrease) + ')' + '\n')
    text_file.write('Average Revenue Change: $' + str(average_change) + '\n')


#open in terminal (with open(filename, "r") as r:)
with open('Output.txt', 'r') as r:
    print(r.read())

