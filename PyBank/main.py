import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


months = []
profit_losses = []
average_change = []
profit_change = []

with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
#    print(csvreader)
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        profit_losses.append(int(row[1]))
        months.append(str(row[0]))
        

total_months = len(months)

print(total_months)
print("Total Profit/Losses: $ " + str(sum(profit_losses)))
# 1) total number of months, 2)total net profit done (8/17)

for a in range(len(profit_losses)-1):
    profit_change.append(profit_losses[a + 1] - profit_losses[a])

average_change = (sum(profit_change) / len(profit_change))
max_increase = max(profit_change)
max_decrease = min(profit_change)

print(f"Average: {average_change}")
print(f"The greatest increase in profits is $ {max_increase}, and the greatest decrease in profits is $ {max_decrease}")
# 3) 4) & 5) greatest increase/decrease done