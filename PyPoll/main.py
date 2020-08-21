import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

vote = []
candidates = []
candidate_vote = []
count = 0

vote_pct = []

total_vote = 0


with open(csvpath, "r") as csvfile:
     csvreader = csv.reader(csvfile, delimiter = ',')
     csv_header = next(csvreader)

     for row in csvreader:
          vote.append(int(row[0]))
          
          candidate_name = row[2]
          if candidate_name in candidates:
               candidate_index = candidates.index(candidate_name)
               candidate_vote[candidate_index] = candidate_vote[candidate_index] + 1
          else:
               candidates.append(candidate_name)
               candidate_vote.append(1)


total_num_vote = len(vote)

#print(total_num_vote)


print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_num_vote} ")
print("-------------------------------------")

for a in range(len(candidates)):
     print(f"{candidates[a]} : {candidate_vote[a]}")