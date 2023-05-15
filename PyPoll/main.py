# Modules
import os
import csv

# Path to votes data file
poll_data = os.path.join("Resources", "election_data.csv")

# Declaring lists for storing data
header_row = []
votes_data = []
cand_name_list = []
cand_count_list = []
cand_perc_list = []
tot_votes_count = 0

# Open votes data file as read
with open(poll_data) as readfile:
    csvreader = csv.reader(readfile)
    # Store headers and move to next row for next steps
    header_row = next(readfile)

    for row in csvreader:
        # Count the total votes
        tot_votes_count = tot_votes_count + 1
        # Copy the candidate votes into a list
        votes_data.append(row[2])

# Sort the votes list and rewrite it into new sorted list
votes_data_s = sorted(votes_data)

# Record the first candidate's name and assign first vote 
cand_name_list.append(votes_data_s[0])
c_votes_count = 1

# Starting second vote (first is already recorded) complete a comparison below
for i in range(len(votes_data_s)-1):
    # If coming across a new candidate name
    if votes_data_s[i+1] != votes_data_s[i]:
        # Record the new candidate's name
        cand_name_list.append(votes_data_s[i+1])
        # Record their vote count into separate list
        cand_count_list.append(c_votes_count)
        # Reset the vote count to 1
        c_votes_count = 1
    else:
        # Keep recording the vote count if candidate's name continues
        c_votes_count = c_votes_count +1
# Record the vote count of the LAST candidate (for loop excludes this step)
cand_count_list.append(c_votes_count)

# Calculate the percentages of votes
for i in range(len(cand_count_list)):
    cand_perc_list.append(round((cand_count_list[i]/tot_votes_count)*100, 3))


# Created a function to check for the max number of votes and to return the winner's name
def find_winner(candidates, votes):
        maxvotes = 0
        for i in range(len(candidates)):
             if votes[i] > maxvotes:
                maxvotes = votes[i]
                winnername = candidates[i]
        return winnername 

# Store the function's result
winner = find_winner(cand_name_list, cand_count_list)

# Set a path to output file
outputfile = os.path.join("analysis", "analysis.txt")

# Open the output file
with open(outputfile, "w") as file:
    # Write the lines inserting analysis results
    file.writelines(["Election Results\n", "-------------------------\n", f"Total Votes: {tot_votes_count}\n", "-------------------------\n"])
    for i in range(len(cand_count_list)):
        file.writelines([f"{cand_name_list[i]}: {cand_perc_list[i]}% ({cand_count_list[i]})\n"])
    file.writelines(["-------------------------\n", f"Winner: {winner}\n", "-------------------------"])

# Print results to terminal
print(" Election Results\n", "-------------------------\n", f"Total Votes: {tot_votes_count}\n", "-------------------------\n")
for i in range(len(cand_count_list)):
        print(f" {cand_name_list[i]}: {cand_perc_list[i]}% ({cand_count_list[i]})\n")
print(" -------------------------\n", f"Winner: {winner}\n", "-------------------------")