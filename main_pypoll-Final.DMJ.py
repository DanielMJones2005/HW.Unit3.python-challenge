# Import Modules
import os
import csv

VoterID = []
County = []
Candidate = []
Candidate2 = []
candidate_list = []
candidate_vote = []
candidate_percent = []

# Set path for file
csvfile = os.path.join("Resources", "election_data.csv")

# Open and read csv
    # Read through each row of data after the header
with open(csvfile, mode="r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    for row in csvreader:    
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
    
    Candidate2 = Candidate.copy()

#Request 1) The total number of votes cast 
    total_votes = len(VoterID) - 1
  
#Request 2) A complete list of candidates who received votes
# traverse for all elements 
    for Candidate in Candidate[1:]:
        # check if exists in unique_list or not 
        if str(Candidate) not in candidate_list: 
            candidate_list.append(Candidate)    

#Request 4) The total number of votes each candidate won   
    for row in candidate_list[0:]:
        irow = (candidate_list.index(row))
        vote_count = (Candidate2.count(str(candidate_list[irow])))
        candidate_vote.append(vote_count)

#Request 3) The percentage of votes each candidate won
        vote_percent = round((vote_count / total_votes)*100,4)
        candidate_percent.append(vote_percent)
 
#Request 5) The winner of the election based on popular vote.
    winner_vote = max(candidate_vote)
    winner_row = candidate_vote.index(winner_vote)
    winner = (str(candidate_list[winner_row]))


#================================================================================================
#================================================================================================

#Title
    print("Election Results")
    print(" ")
    print("---------------------------")
    print(" ")

#Request 1) The total number of votes cast 
    print("Total Votes: " + str(total_votes))
    print(" ")
    print("---------------------------")

#Request 2) #A complete list of candidates who received votes
#Request 3) The percentage of votes each candidate won
    print(" ")
    print(str(candidate_list[0]) + ": " + str(candidate_percent[0]) + "00% " + "(" +  str(candidate_vote[0]) + ")")
    print(str(candidate_list[1]) + ": " + str(candidate_percent[1]) + "00% " + "(" +  str(candidate_vote[1]) + ")")
    print(str(candidate_list[2]) + ": " + str(candidate_percent[2]) + "00% " + "(" +  str(candidate_vote[2]) + ")")
    print(str(candidate_list[3]) + ": " + str(candidate_percent[3]) + "00% " + "(" +  str(candidate_vote[3]) + ")")
    print(" ")
    
#Request 4) The winner of the election based on popular vote.
    print("---------------------------")
    print("Winner: " + winner)
    print("---------------------------")


#================================================================================================
#================================================================================================

#Send to Text
myFile = open('pypoll_analysis.txt', 'w')
with myFile: 

    #Title
    myFile.write("Election Results\n")
    myFile.write(" \n")
    myFile.write("---------------------------\n")
    myFile.write(" \n")

#Request 1) The total number of votes cast 
    myFile.write("Total Votes: " + str(total_votes) + "\n")
    myFile.write(" ")
    myFile.write("---------------------------\n")

#Request 2) #A complete list of candidates who received votes
#Request 3) The percentage of votes each candidate won
    myFile.write(" \n")
    myFile.write(str(candidate_list[0]) + ": " + str(candidate_percent[0]) + "00% " + "(" +  str(candidate_vote[0]) + ")\n")
    myFile.write(str(candidate_list[1]) + ": " + str(candidate_percent[1]) + "00% " + "(" +  str(candidate_vote[1]) + ")\n")
    myFile.write(str(candidate_list[2]) + ": " + str(candidate_percent[2]) + "00% " + "(" +  str(candidate_vote[2]) + ")\n")
    myFile.write(str(candidate_list[3]) + ": " + str(candidate_percent[3]) + "00% " + "(" +  str(candidate_vote[3]) + ")\n")
    myFile.write(" \n")
    
#Request 4) The winner of the election based on popular vote.
    myFile.write("---------------------------\n")
    myFile.write("Winner: " + winner + "\n")
    myFile.write("---------------------------\n")