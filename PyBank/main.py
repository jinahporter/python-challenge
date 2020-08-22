import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
#csvpath = os.path.join('..','PyBank','Resources', 'budget_data.csv')

months = []
profit_losses = []
average_change = []
profit_change = []

with open(csvpath, "r") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        profit_losses.append(int(row[1]))
        months.append(str(row[0]))
        
total_months = len(months)

print("Financial Analysis")
print("---------------------------------------------")
print(f"Total Months: {total_months}")
print("Total: $ " + str(sum(profit_losses)))
# 1) total number of months, 2)total net profit done (8/17)

# 3, 4, 5 start below
for a in range(len(profit_losses)-1):
    profit_change.append(profit_losses[a + 1] - profit_losses[a])

average_change = (sum(profit_change) / len(profit_change))
max_increase = max(profit_change)
max_decrease = min(profit_change)

print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: ($ {max_increase})")
print(f"Greatest Decrease in Profits: ($ {max_decrease})")
# 3) 4) & 5) greatest increase/decrease done