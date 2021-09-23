# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
#declare new list for candidate 
candidate_options=[]
candidate_votes={}
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
         total_votes += 1
# Print the candidate name from each row
         candidate_name = row[2]
        # If the candidate does not match any existing candidate...
         if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
 # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
   # Add a vote to that candidate's count.
         candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
# 3. Print the total votes.
print(candidate_votes)