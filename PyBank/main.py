import os
import csv

#csvpath = os.path.join('..', 'Resources', 'election_data.csv')
csv_file = 'PyBank/Resources/budget_data.csv'

with open(csv_file, 'r') as file_handler:
     lines = file_handler.read()
     print(lines)
     print(type(lines))