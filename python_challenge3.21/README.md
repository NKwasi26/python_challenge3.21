# python_challenge3.21
#PyPoll
import os
import csv

# provide file path
file_path = os.path.join('Resources','election_data.csv')
output_path = os.path.join('analysis','election_analysis.txt')

# name variables
total_votes = 0
candidate_a = 'Charles Casper Stockham'
charles_casper_votes = 0
candidate_b = 'Diana DeGette'
diana_degette_votes = 0
candidate_c = 'Raymon Anthony Doane'
raymon_anthony_votes = 0


with open(file_path, 'r') as csvfile:
  csv_reader = csv.reader(csvfile, delimiter=",")


  #Read the header row
csv_header = next(csv_reader)
  #Iterate through each row in the file starting after the header
for row in csv_reader: 
    #calculate total votes
    total_votes +=1
    
    #list of candidates who won
    if row[2] == candidate_a:
        charles_casper_votes +=1

    elif row[2] == candidate_b:
        diana_degette_votes +=1

    elif row[2] == candidate_c:
        raymon_anthony_votes +=1
    
#calculate percentages of votes won 
    css_percentage = round(charles_casper_votes/total_votes * 100, 3)
    ddg_percentage = round(diana_degette_votes/total_votes * 100, 3)
    rad_percentage = round(raymon_anthony_votes/total_votes * 100, 3)

#determine winner
    votes = [charles_casper_votes, diana_degette_votes, raymon_anthony_votes]
    candidates = [candidate_a, candidate_b, candidate_c]
    winner = candidates[votes.index(max(votes))]

   
#prepare output for print
output = ("\nElection Results\n"
          f"\n------------------------------'\n\n"
  f"Total Votes: {total_votes}\n"
  f"\n------------------------------'\n"
  f"Charles Casper Stockham: {css_percentage}% ({charles_casper_votes})\n"
  f"Diana DeGette: {ddg_percentage}% ({diana_degette_votes})\n"
  f"Raymon Anthony Doane: {rad_percentage}% ({raymon_anthony_votes})\n"
  f"\n------------------------------\n"
  f"\nWinner: {winner}\n"
  f"\n------------------------------\n")

#print output
print(output)

#write to txtfile and save in output path
with open(output_path, "w") as txtfile: 
   txtfile.write(output)
 
