import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

vote = []
candidates = []

with open(csvpath, "r") as csvfile:
     csvreader = csv.reader(csvfile, delimiter = ',')
     csv_header = next(csvreader)

     for row in csvreader:
        vote.append(int(row[0]))
        candidates.append(row[2])

list_of_candidates = set(candidates)
new_list_of_candidates = list(list_of_candidates)


total_num_vote = len(vote)

print(total_num_vote)
print(new_list_of_candidates)

