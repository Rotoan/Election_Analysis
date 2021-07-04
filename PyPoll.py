import csv
import os


#1. data we need to retrieve
###open file and load election data
File_to_load = ('Resources/election_results.csv')
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(File_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)
### perform analysis
    headers =  next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = round(float(votes) / float(total_votes) * 100, 1)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        print(winning_candidate_summary)
        

### close file

#                election_data.close()

#2. total number of votes cast
#3. complete list of candidates that received votes
#4. vote totals per candidate
#5. percentage vote total for all candidates
#6. election winner based on popular vote 


