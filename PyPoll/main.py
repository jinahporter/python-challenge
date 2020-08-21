import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

vote = []
candidates = []
candidate_vote = []
percentage = []

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
#print(new_list_of_candidates)

print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_num_vote} ")
print("-------------------------------------")


for a in range(len(candidates)):
     percentage = {(candidate_vote[a]) / (total_num_vote)} * 100
     print(f"{candidates[a]} : {percentage} %, {candidate_vote[a]}")