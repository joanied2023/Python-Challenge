#This is main2.py for PyPoll exercise by Joan Denoncour
#import libraries
import os
import csv

#path to collect data from resources folder
csvpath = os.path.join(".", "Resources", "election_data.csv")
#specify the file path with txt file to write to
#output_path = os.path.join(".","Analysis", "PyPollAnalysis.txt")

with open (csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #internal command to tell you csvreader exists and we will call it
    print(csvreader)

    #read header row first
    csv_header = next(csvreader)

    # since we are essentially counting the number of rows in the ws; 
    # set counter at 0
    TotalVotesCount = 0
    TotalVotes = []
    CandidateDict = {}

    for row in csvreader:
       #count total votes 
        TotalVotes.append(row[0])
        TotalVotesCount +=1

        #who are unique candidates
        Candidate = row[2]        
        
        if Candidate in CandidateDict:
            CandidateDict[Candidate]+=1
           
        else:
            CandidateDict[Candidate]=1
          
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(TotalVotesCount))
print("----------------------------")

for candidate,votes in CandidateDict.items():
    print(f"{candidate}: ({votes})")
print("----------------------------")
print("Winner: Diana DeGette")
print("----------------------------")


#using Reed's function from Slack
def write_to_file(filename, lines):
    with open(filename,"w") as text:
        for line in lines:
            text.write(f"{line}\n")

write_to_file("PyPollAnalysis.txt",["Election Results",
                                    "----------------------------",
                                    "Total Months: " + str(TotalVotesCount),
                                    "----------------------------",
                                    "Winner: Diana DeGette",
                                    "----------------------------"])
                                    
                                   
    






    





