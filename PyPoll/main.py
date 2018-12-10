#import os and csv files
import os
import csv

# variables
candidates = []
voteNumber = 0
voteCount = []

#path

electionCSV = os.path.join('Resources','election_data.csv')


#open the file
with open(electionCSV,newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        voteNumber = voteNumber + 1
        
        candidate =row[2]
        

        if candidate in candidates:
            candidate_in = candidates.index(candidate)
            voteCount[candidate_in] = voteCount[candidate_in]+1
        else:
            candidates.append(candidate)
            voteCount.append(1)

percentages =[]
mostVote = voteCount[0]
indexMost=0

for count in range(len(candidates)):
    votePercent = voteCount[count]/voteNumber*100
    percentages.append(votePercent)
    if voteCount[count] > mostVote:
        mostVote = voteCount[count]
        print(mostVote)
        
winner = candidates[indexMost]

print("Election Results")
print('-----------')
print(f"Total Votes: {voteNumber}")
print('-----------')
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({voteCount[count]})")
print('-----------')
print(f"Winner: {winner}")

write_file = f"pypoll_results_summary.txt"

#open write file
filewriter = open(write_file, mode = 'w')

#print analysis to file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {voteNumber}\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({voteCount[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

#close file
filewriter.close()