import os
import csv

#csvpath = os.path.join('..', 'Resources', 'election_data.csv')
csv_file = '/Users/jinahporter/Dropbox/내 Mac (Jinah의 MacBook Pro)/Desktop/Rice 2020/python-challenge/PyPoll/Resources/election_data.csv'

with open(csv_file, 'r') as file_handler:
     lines = file_handler.read()
     print(lines)
     print(type(lines))