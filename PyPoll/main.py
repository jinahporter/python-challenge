import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_vote = 0

candidates = []
candidate_vote = {}

vote_percentage = 0
votes = 0
winning_cand = ""
winning_count = 0

with open(csvpath, "r") as csvfile:
     csvreader = csv.reader(csvfile, delimiter = ',')
     csv_header = next(csvreader)

     for row in csvreader:
         #vote.append(int(row[0]))
         #count total vote
         total_vote += 1
          
         candidate_name = row[2]
         if candidate_name not in candidates:
             candidates.append(candidate_name)
             candidate_vote[candidate_name]= 0
         candidate_vote[candidate_name] +=1

print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_vote} ")
print("-------------------------------------")

#working on percentage and the vote count for each candidate
for candidate_name in candidate_vote:
     votes = candidate_vote[candidate_name]
     vote_percentage= (votes / total_vote) *100

     if (candidate_vote[candidate_name] > winning_count):
         winning_count = candidate_vote[candidate_name]
         winning_cand = candidate_name
     
     results = f"{candidate_name}: {vote_percentage}% ({votes})\n"
     print(results)

print("-------------------------------------")
print(f"The Winner: {winning_cand}")
print("-------------------------------------")